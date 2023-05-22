import { createClient } from "redis";

const subscriber = createClient();

subscriber
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
  });

subscriber.subscribe("holberton school channel");

subscriber.on("message", (channel, message) => {
  if (message === "KILL_SERVER") {
    subscriber.unsubscribe("holberton school channel");
    subscriber.quit();
  }
  console.log(message);
});
