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
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

// Process the jobs
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
