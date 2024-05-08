import kue from 'kue';

// Create a queue instance
const queue = kue.createQueue();

// Define job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Your verification code is 1234',
};

// Create a job in the queue
const job = queue.create('push_notification_code', jobData).save((error) => {
  if (!error) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});
job.on('failed', () => {
  console.log('Notification job failed');
});
