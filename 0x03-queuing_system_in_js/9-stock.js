const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const port = 1245;

// Redis client setup
const client = redis.createClient();
const listProducts = [
  {
    id: 1, name: 'Suitcase 250', price: 50, stock: 4,
  },
  {
    id: 2, name: 'Suitcase 450', price: 100, stock: 10,
  },
  {
    id: 3, name: 'Suitcase 650', price: 350, stock: 2,
  },
  {
    id: 4, name: 'Suitcase 1050', price: 550, stock: 5,
  },
];
app.use(express.json());

function getItemById(id) {
  const item = listProducts.find((product) => product.id === id);
  if (item) {
    return Object.fromEntries(Object.entries(item));
  }
}

const reserveStockById = async (itemId, stock) => promisify(client.SET).bind(client)(`item.${itemId}`, stock);

const getCurrentReservedStockById = async (itemId) => promisify(client.GET).bind(client)(`item.${itemId}`);

// Route to get the list of products
app.get('/list_products', (req, res) => {
  res.json(listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  })));
});

// Route to get product details by ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number.parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  const result = await getCurrentReservedStockById(itemId);
  const currentReservedStock = Number.parseInt(result || 0);
  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity: product.stock - currentReservedStock,
  });
});

// Route to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number.parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }
  const result = await getCurrentReservedStockById(itemId);
  const currentReservedStock = Number.parseInt(result || 0, 10);
  if (currentReservedStock >= product.stock) {
    res.json({ status: 'Not enough stock available', itemId });
    return;
  }

  // Reserve stock
  await reserveStockById(itemId, currentReservedStock + 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

const resetProductsStock = async () => Promise.allSettled(
  listProducts.map(
    (item) => promisify(client.SET).bind(client)(`item.${item.itemId}`, 0),
  ),
);
app.listen(port, () => {
  resetProductsStock().then(() => console.log(`Server running on port ${port}`));
});
