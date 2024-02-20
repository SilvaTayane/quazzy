var array_reaction = document.getElementsByClassName('reaction-button');

for (var i = 0; i < array_reaction.length; i++) {
  array_reaction[i].addEventListener('click', function () {
    var icon = this.querySelector('i');
    if (icon.classList.contains('bi-heart')) {
      icon.classList.remove('bi-heart');
      icon.classList.add('bi-heart-fill');
    } else {
      icon.classList.remove('bi-heart-fill');
      icon.classList.add('bi-heart');
    }
  });
}
