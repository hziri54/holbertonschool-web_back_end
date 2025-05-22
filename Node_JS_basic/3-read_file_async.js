const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      } else {
        const lines = data.trim().split('\n').filter((line) => line.trim() !== ''); // Filter out empty lines

        if (lines.length <= 1) {
          reject(new Error('Cannot load the database'));
        } else {
          const students = lines.slice(1).map((line) => line.split(','));

          console.log(`Number of students: ${students.length}`);

          const fields = {};
          students.forEach((student) => {
            const field = student[3];
            const firstName = student[0];

            if (!fields[field]) {
              fields[field] = [];
            }
            fields[field].push(firstName);
          });

          for (const [field, firstNames] of Object.entries(fields)) {
            console.log(`Number of students in ${field}: ${firstNames.length}. List: ${firstNames.join(', ')}`);
          }

          resolve();
        }
      }
    });
  });
}

module.exports = countStudents;
