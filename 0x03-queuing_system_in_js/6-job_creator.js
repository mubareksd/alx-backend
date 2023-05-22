import { createQueue } from "kue";

const queue = createQueue();

const notification = {
  phoneNumber: "0900000000",
  message: "This is a message.",
};

const job = queue.create("push_notification_code", notification).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job
  .on("complete", () => {
    console.log("Notification job completed");
  })
  .on("failed", () => {
    console.log("Notification job failed");
  });
