#!/usr/bin/env node
// Create an array that will contain the blacklisted phone numbers.

import { createQueue, Job } from 'kue';

// Create a new Kue queue
const queue = createQueue();

// Define an array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

/**
 * Sends a notification to a phone number with a given message.
 * @param {string} phoneNumber - The phone number to send the notification to.
 * @param {string} message - The message to send in the notification.
 * @param {Object} job - The Kue job object being processed.
 * @param {function} done - The function to call when the job is done processing.
 * @throws {Error} Will throw an error if the phone number is blacklisted.
 * @returns {void}
 */
const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);
  if (blacklistedNumbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
