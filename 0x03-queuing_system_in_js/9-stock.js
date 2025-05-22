import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

// Redis client setup
const redisClient = createClient();
redisClient.on('error', (err) => console.error('Redis error:', err));

const setAsync = promisify(redisClient.set).bind(redisClient);
const getAsync = promisify(redisClient.get).bind(redisClient);

// Product list
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

// Get item by ID
function getItemById(id) {
  return listProducts.find(item => item.itemId === id);
}

// Reserve stock in Redis
async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

// Get reserved stock
async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock !== null ? parseInt(stock) : null;
}

// Express app setup
const app = express();
const port = 1245;

// List all products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Get specific product + stock
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const quantity = currentStock !== null ? currentStock : item.initialAvailableQuantity;

  res.json({ ...item, currentQuantity: quantity });
});

// Reserve product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const availableStock = currentStock !== null ? currentStock : item.initialAvailableQuantity;

  if (availableStock < 1) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  await reserveStockById(itemId, availableStock - 1);
  return res.json({ status: 'Reservation confirmed', itemId });
});

// Start server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
