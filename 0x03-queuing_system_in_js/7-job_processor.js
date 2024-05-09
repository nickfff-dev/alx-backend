import kue from 'kue';

// Create a queue instance
const queue = kue.createQueue();

// Blacklisted phone numbers
const blacklistedNumbers = [
  '4153518780',
  '4153518781',
];

// Define sendNotification function
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  job.progress(100, 100);
  done();
}

// Process the jobs
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

// Log event on job completion
queue.on('job complete', (id, result) => {
  kue.Job.get(id, (err, job) => {
    if (err) return;
    console.log(`Notification job ${job.id} completed`);
  });
});

// Log event on job failure
queue.on('job failed', (id, errorMessage) => {
  kue.Job.get(id, (err, job) => {
    if (err) return;
    console.log(`Notification job ${job.id} failed: ${errorMessage}`);
  });
});
