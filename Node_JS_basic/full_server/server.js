import express from 'express';
import router from './routes/index.js';

const app = express();
const PORT = 1245;

// Use the routes
app.use('/', router);

// Start the server
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});

export default app;
