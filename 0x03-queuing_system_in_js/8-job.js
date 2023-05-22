const createPushNotificationsJobs = (jobs, queue) => {
  if (!(jobs instanceof Array)) throw Error("Jobs is not an array");
  jobs.forEach((job) => {
    const pushNotificationJob = queue.create("push_notification_code_2", job);
    pushNotificationJob.save((err) => {
      if (!err)
        console.log(`Notification job created: ${pushNotificationJob.id}`);
    });
    pushNotificationJob.on("complete", () =>
      console.log(`Notification job ${pushNotificationJob.id} completed`)
    );
    pushNotificationJob.on("failed", (err) =>
      console.log(`Notification job ${pushNotificationJob.id} failed: ${err}`)
    );
    pushNotificationJob.on("progress", (progress) =>
      console.log(
        `Notification job ${pushNotificationJob.id} ${progress}% complete`
      )
    );
  });
};

export default createPushNotificationsJobs;
