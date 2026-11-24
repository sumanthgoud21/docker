const express = require('express');
const axios = require('axios');
const path = require('path');
const escapeHtml = require('./escapeHtml');

const app = express();
const PORT = 3000;
const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000';

// Parse HTML form data & JSON
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Serve index.html automatically on GET /
app.use(express.static(path.join(__dirname, 'views')));

// Bridge route: receives form from browser -> forwards to Flask container
app.post('/submit-form', async (req, res) => {
  try {
    const flaskResponse = await axios.post(`${BACKEND_URL}/submit`, req.body);

    res.send(`
      <h2>Form Processed by Flask Backend!</h2>
      <p><strong>Message:</strong> ${escapeHtml(flaskResponse.data.message)}</p>
      <pre>${escapeHtml(JSON.stringify(flaskResponse.data.processed_data, null, 2))}</pre>
      <a href="/">Go Back</a>
    `);
  } catch (error) {
    console.error('Flask connection error:', error.message);
    const message = error.response?.data?.error || 'The Flask backend could not be reached.';
    const status = error.response?.status || 502;
    res.status(status).send(`
      <h3>Form submission failed</h3>
      <p>${escapeHtml(message)}</p>
      <a href="/">Try Again</a>
    `);
  }
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Express frontend listening on http://0.0.0.0:${PORT}`);
});