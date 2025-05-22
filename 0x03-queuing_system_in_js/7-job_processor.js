import kue from 'kue';

const queue = kue.createQueue();

// Define blacklisted numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

/**
 * Job processor function
 * @param {string} phoneNumber
 * @param {string} message
 * @param {object} job
 * @param {function} done
 */
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100); // Set initial progress

  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100); // Midway progress

  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  done(); // Mark job as done
}

// Process jobs from push_notification_code_2, 2 at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
