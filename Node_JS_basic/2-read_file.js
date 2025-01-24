const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8').trim();

    const rows = data.split('\n').filter((row) => row.trim() !== '');

    if (rows.length <= 1) {
      throw new Error('Cannot load the database');
    }

    const students = rows.slice(1).map((row) => row.split(','));

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
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
