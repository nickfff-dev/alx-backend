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

// Function to set a new school value in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Function to display the value of a school in Redis
function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, reply) => {
    if (error) {
      console.log(error.message);
    } else {
      console.log(reply);
    }
  });
}

// Example usages
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
