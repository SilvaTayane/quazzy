document.getElementById('reactionButton').addEventListener('click', function() {
    var icon = this.querySelector('i');
    if (icon.classList.contains('bi-heart')) {
      icon.classList.remove('bi-heart');
      icon.classList.add('bi-heart-fill');
    } else {
      icon.classList.remove('bi-heart-fill');
      icon.classList.add('bi-heart');
    }
  });
  