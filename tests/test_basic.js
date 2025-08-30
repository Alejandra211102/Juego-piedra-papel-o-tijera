const request = require('supertest');
const app = require('../app'); // ajusta la ruta
describe('Basic Tests', () => {
test('should respond to GET /', async () => {
const response = await request(app).get('/');
expect(response.statusCode).toBe(200);
});
});
# .github/workflows/ci.yml
name: js_test
on:
push:
