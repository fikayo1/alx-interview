#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + id, async function (error, res, body) {
  if (error) {
    console.error('error:', error);
    return;
  }

  if (res && res.statusCode === 200) {
    const data = JSON.parse(body);
    console.log('status code:', res.statusCode);
    const characters = data.characters;

    for (let i = 0; i < characters.length; i++) {
      const characterURL = characters[i];
      const characterData = await getCharacterData(characterURL);
      console.log(characterData.name);
    }
  } else {
    console.log('status code:', res && res.statusCode);
  }
});

function getCharacterData (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (error) {
        reject(error);
        return;
      }

      if (res && res.statusCode === 200) {
        const characterData = JSON.parse(body);
        resolve(characterData);
      } else {
        reject(new Error('Request failed with status code: ' + res.statusCode));
      }
    });
  });
}
