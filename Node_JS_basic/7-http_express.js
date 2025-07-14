const express = require('express');
const countStudents = require('./3-read_file_async');
const path = require('path');

const app = express();
const database = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudents(database)
    .then((output) => {
      res.setHeader('Content-Type', 'text/plain');
      res.send(`This is the list of our students\n${output}`);
    })
    .catch(() => {
      res.status(500).send('Cannot load the database');
    });
});

app.listen(1245);

module.exports = app;
