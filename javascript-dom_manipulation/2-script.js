const header = document.querySelector('header');
const redheader = document.querySelector('#red_header');

redheader.addEventListener('click', function () {
  header.classList.add('red');
});
