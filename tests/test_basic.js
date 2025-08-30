// app.test.js
const request = require('supertest');
const app = require('./app'); // Ruta al archivo de tu servidor

describe('Basic GET / test', () => {
  test('should respond with status 200', async () => {
    const response = await request(app).get('/');
    expect(response.statusCode).toBe(200);
    expect(response.text).toBe('Hello World');
  });
});
