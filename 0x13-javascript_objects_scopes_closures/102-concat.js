#!/usr/bin/node

const fs = require('fs').promises;
const { argv } = require('process');

if (argv.length !== 5) {
  console.error('Usage: ./script.js source_file1 source_file2 destination_file');
  process.exit(1);
}

const sourceFile1 = argv[2];
const sourceFile2 = argv[3];
const destinationFile = argv[4];

fs.readFile(sourceFile1, 'utf8')
  .then(data => {
    return fs.writeFile(destinationFile, data, 'utf8');
  })
  .then(() => {
    return fs.readFile(sourceFile2, 'utf8');
  })
  .then(data => {
    return fs.writeFile(destinationFile, data, { flag: 'a' }, 'utf8');
  })
  .then(() => {
    console.log('Files concatenated successfully.');
  })
  .catch(err => {
    console.error(err);
  });
