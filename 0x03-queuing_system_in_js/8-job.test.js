// Import the necessary modules
import { expect } from 'chai';
import { createQueue } from 'kue';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job';

const queue = createQueue();

describe('createPushNotificationsJobs', () => {
  const myspy = sinon.spy(console, 'log');
  before(() => {
    queue.testMode.enter(true);
  });

  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });
  
  afterEach(() => {
    myspy.resetHistory();
  });
  // Test case: jobs is not an array
  it('display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw(Error, 'Jobs is not an array');
  });

  // Test case: create two new jobs to the queue
  it('create two new jobs to the queue', (done) => {
    expect(queue.testMode.jobs).to.have.lengthOf(0);
    const jobs = [
      { phoneNumber: '1234567890', message: 'Hello' },
      { phoneNumber: '0987654321', message: 'World' },
    ];
    createPushNotificationsJobs(jobs, queue);
      expect(queue.testMode.jobs.length).to.equal(2);
      expect(queue.testMode.jobs[0].data.phoneNumber).to.equal('1234567890');
      expect(queue.testMode.jobs[0].data.message).to.equal('Hello');
      expect(queue.testMode.jobs[1].data.phoneNumber).to.equal('0987654321');
      expect(queue.testMode.jobs[1].data.message).to.equal('World');
      expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
      queue.process('push_notification_code_3', () => {
        expect(myspy.calledWith(`Notification job created: ${queue.testMode.jobs[0].id}`)).to.be.true;
        expect(myspy.calledWith(`Notification job created: ${queue.testMode.jobs[1].id}`)).to.be.true;
        done();
      });
 
     
  });

  // Test case: job progress
  it('display a progress of 50% for the first job', (done) => {  
    queue.testMode.jobs[0].addListener('progress', () => {
      // check the console output
      expect(myspy.calledWith(`Notification job ${queue.testMode.jobs[0].id} 50% complete`)).to.be.true;
      done();
    })
    queue.testMode.jobs[0].emit('progress', 50);
  });

  // Test case: job completion
  it('display a completion message for the first job', (done) => {
    queue.testMode.jobs[0].addListener('complete', () => {
      // check the console output
      expect(myspy.calledWith(`Notification job ${queue.testMode.jobs[0].id} completed`)).to.be.true;
      done();
    });
    queue.testMode.jobs[0].emit('complete');
  });

  // Test case: job failure
  it('display a failure message for the first job', (done) => {
    queue.testMode.jobs[0].addListener('failed', () => {
      // check the console output
      expect(myspy.calledWith(`Notification job ${queue.testMode.jobs[0].id} failed`)).to.be.true;
      done();
    });
    queue.testMode.jobs[0].emit('failed');
  });
});
