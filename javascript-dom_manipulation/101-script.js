document.addEventListener('DOMContentLoaded', function () {
  const box = document.getElementById('language_code');
  const btn = document.getElementById('btn_translate');
  const hello = document.getElementById('hello');

  btn.addEventListener('click', function () {
    fetch(`https://hellosalut.stefanbohacek.com/?lang=${box.value}`)
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        hello.textContent = data.hello;
      });
  });
});
