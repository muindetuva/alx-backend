import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print); // print logs a confirmation message
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error retrieving value for ${schoolName}: ${err}`);
    } else {
      console.log(reply);
    }
  });
}

// Call the functions
displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');
