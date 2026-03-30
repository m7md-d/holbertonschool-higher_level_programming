document.addEventListener('DOMContentLoaded', function () {
  const myList = document.querySelector('.my_list');
  const addItem = document.getElementById('add_item');
  const removeItem = document.getElementById('remove_item');
  const clearList = document.getElementById('clear_list');
  const newItem = '<li>Item</li>';

  addItem.addEventListener('click', function () {
    myList.insertAdjacentHTML('beforeend', newItem);
  });

  removeItem.addEventListener('click', function () {
    const lastItem = myList.lastElementChild;

    if (lastItem) {
      lastItem.remove();
    }
  });

  clearList.addEventListener('click', function () {
    myList.innerHTML = '';
  });
});
