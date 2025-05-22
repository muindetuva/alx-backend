import kue from 'kue';

// Create the queue
const queue = kue.createQueue();

// Create job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Your verification code is 1234',
};

// Create the job
const job = queue.create('push_notification_code', jobData);

// Save the job to Redis
job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

// Listen for job events
job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
