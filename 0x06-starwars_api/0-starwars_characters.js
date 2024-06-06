#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + movieId,
  method: 'GET'
};

request(options, function (error, response, body) {
  if (error || response.statusCode !== 200) {
    console.error('Failed to fetch movie information:', error || `Status code: ${response.statusCode}`);
    process.exit(1);
  }

  const characters = JSON.parse(body).characters;
  if (characters.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  printCharacters(characters, 0);
});

function printCharacters(characters, index) {
  if (index >= characters.length) return;

  request(characters[index], function (error, response, body) {
    if (error || response.statusCode !== 200) {
      console.error('Failed to fetch character information:', error || `Status code: ${response.statusCode}`);
      return;
    }

    console.log(JSON.parse(body).name);
    printCharacters(characters, index + 1);
  });
}
