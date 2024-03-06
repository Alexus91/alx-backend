#!/usr/bin/env node
// Create a queue with Kue

import { createQueue } from 'kue';

// create the queue
const queue = createQueue();

const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
};

// queue process that will listen to new jobs on push_notification_code
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});

export default queue;
