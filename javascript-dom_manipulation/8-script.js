document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      const helloElement = document.getElementById('hello');
      helloElement.textContent = data.hello;
    });
});
