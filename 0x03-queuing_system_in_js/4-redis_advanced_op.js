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

// Function to create a hash in Redis
function createHash(hashName, hashValues) {
  Object.keys(hashValues).forEach((key) => {
    client.hset(hashName, key, hashValues[key], redis.print);
  });
}

// Function to display the hash stored in Redis
function displayHash(hashName) {
  client.hgetall(hashName, (error, reply) => {
    if (error) {
      console.log(error.message);
    } else {
      console.log(reply);
    }
  });
}

// Example usage
const hashValues = {
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2',
};

createHash('HolbertonSchools', hashValues);
displayHash('HolbertonSchools');
