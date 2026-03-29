const header = document.querySelector('header');
const toggleheader = document.querySelector('#toggle_header');

toggleheader.addEventListener('click', function () {
  header.classList.toggle('green');
  header.classList.toggle('red');
});
