const express = require('express');
const fs = require('fs');

const app = express();
const PORT = 1245;

const countStudents = (databasePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(databasePath, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const studentsByField = {};
      let totalStudents = 0;

      for (const line of lines.slice(1)) {
        const parts = line.split(',');
        if (parts.length >= 4 && parts[3]) {
          const field = parts[3];
          const firstName = parts[0];
          if (!studentsByField[field]) studentsByField[field] = [];
          studentsByField[field].push(firstName);
          totalStudents++;
        }
      }

      let output = `This is the list of our students\n`;
      output += `Number of students: ${totalStudents}`;
      for (const field in studentsByField) {
        output += `\nNumber of students in ${field}: ${studentsByField[field].length}. List: ${studentsByField[field].join(', ')}`;
      }

      resolve(output);
    });
  });
};

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.set('Content-Type', 'text/plain');
  const databasePath = process.argv[2];
  try {
    const result = await countStudents(databasePath);
    res.send(result);
  } catch (err) {
    res.status(500).send(err.message);
  }
});

app.listen(PORT);

module.exports = app;

