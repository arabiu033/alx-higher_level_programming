// Write a JavaScript script that fetches and lists the title
// for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
$.get('https://swapi.co/api/films/?format=json', function (data) {
  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});