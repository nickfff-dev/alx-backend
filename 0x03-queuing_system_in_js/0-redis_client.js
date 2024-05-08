import redis from 'redis';

// Create a client instance
const client = redis.createClient();

// Add a 'connect' event listener
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Add an 'error' event listener
client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});
