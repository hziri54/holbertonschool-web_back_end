const express = require("express");
const fs = require("fs");

const app = express();
const PORT = 1245;

const countStudents = (databasePath) => {
    return new Promise((resolve, reject) => {
        fs.readFile(databasePath, "utf-8", (err, data) => {
            if (err) {
                reject("Cannot load the database");
                return;
            }

            const lines = data.split("\n").filter(line => line.trim() !== "");
            const students = {};
            let totalStudents = 0;

            lines.slice(1).forEach((line) => {
                const parts = line.split(",");
                const field = parts[3]; 
                const firstName = parts[0];

                if (field) {
                    if (!students[field]) students[field] = [];
                    students[field].push(firstName);
                    totalStudents++;
                }
            });

            let result = `This is the list of our students\nNumber of students: ${totalStudents}`;
            for (const field in students) {
                result += `\nNumber of students in ${field}: ${students[field].length}. List: ${students[field].join(", ")}`;
            }

            resolve(result);
        });
    });
};

app.get("/", (req, res) => {
    res.send("Hello Holberton School!");
});

app.get("/students", async (req, res) => {
    const databasePath = process.argv[2]; 
    try {
        const studentsList = await countStudents(databasePath);
        res.send(studentsList);
    } catch (error) {
        res.status(500).send(error);
    }
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

module.exports = app;
