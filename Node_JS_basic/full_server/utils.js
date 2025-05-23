import fs from 'fs';

export function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) return reject(new Error('Cannot load the database'));

      const lines = data.trim().split('\n');
      const headers = lines[0].split(',');
      const studentsByField = {};

      for (const line of lines.slice(1)) {
        const student = line.split(',');
        const field = student[3];
        const firstName = student[0];
        if (!studentsByField[field]) studentsByField[field] = [];
        studentsByField[field].push(firstName);
      }

      resolve(studentsByField);
    });
  });
}
