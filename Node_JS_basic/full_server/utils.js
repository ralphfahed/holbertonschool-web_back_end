import fs from 'fs';

/**
 * Reads the database file and returns an object of arrays of student firstnames per field
 * @param {string} filePath - Path to the CSV database file
 * @returns {Promise<Object>} Promise that resolves to an object with field names as keys and arrays of firstnames as values
 */
const readDatabase = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter(line => line.trim() !== '');
      
      if (lines.length <= 1) {
        resolve({});
        return;
      }

      const students = lines.slice(1); // Remove header
      const validStudents = students.filter(student => student.split(',').length >= 4);
      
      const fields = {};
      
      validStudents.forEach(student => {
        const [firstname, , , field] = student.split(',');
        if (firstname && field) {
          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
        }
      });

      resolve(fields);
    });
  });
};

export default readDatabase;
