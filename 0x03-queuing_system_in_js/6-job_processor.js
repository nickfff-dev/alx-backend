import kue from 'kue';

// Create a queue instance
const queue = kue.createQueue();

// Define the sendNotification function
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process the jobs in the queue
queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
