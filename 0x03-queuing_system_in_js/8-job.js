function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array)) throw new Error('Jobs is not an array');
  jobs.forEach((job) => {
    const jobData = {
      phoneNumber: job.phoneNumber,
      message: job.message,
    };
    const createdJob = queue.create('push_notification_code_3', jobData).save((error) => {
      if (!error) console.log(`Notification job created: ${createdJob.id}`);
    });
    createdJob.on('complete', () => {
      console.log(`Notification job ${createdJob.id} completed`);
    });
    createdJob.on('failed', () => {
      console.log(`Notification job ${createdJob.id} failed`);
    });
    createdJob.on('progress', (progress) => {
      console.log(`Notification job ${createdJob.id} ${progress}% complete`);
    });
  });
}
module.exports = createPushNotificationsJobs;
export default createPushNotificationsJobs;
