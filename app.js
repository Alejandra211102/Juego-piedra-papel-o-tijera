// app.js
const express = require('express');
const app = express();

// Ruta básica que responde con "Hello World"
app.get('/', (req, res) => {
  res.status(200).send('Hello World');
});

// Exporta la aplicación para que pueda ser usada en los tests
module.exports = app;
