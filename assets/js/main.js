function toggleMobileMenu() {
    var fab = document.querySelector('.fab');
    fab.classList.toggle('expanded');

    if (fab.classList.contains('expanded')) {
        fab.innerHTML = navigationLinks.map(link => 
            `<a href="${link.url}">${link.title}</a>`
        ).join('') +
        '<div class="fab-close" onclick="closeMobileMenu(event)">✕</div>';
    } else {
        fab.innerHTML = '☰';
    }
}

document.addEventListener('DOMContentLoaded', function() {
  const imageContainers = document.querySelectorAll('.image-container');
  const backgroundOverlay = document.createElement('div');
  backgroundOverlay.classList.add('background-overlay');
  document.body.appendChild(backgroundOverlay); 

  imageContainers.forEach(function(container) {
    const image = container.querySelector('img');

    container.addEventListener('click', function() {
      image.classList.toggle('fade-image');
      image.classList.toggle('active');
      backgroundOverlay.style.display = 'block';
    });
  });

  document.addEventListener('click', function(event) {
    if (!event.target.closest('.image-container')) {
      const activeImage = document.querySelector('.fade-image.active');
      if (activeImage) {
        activeImage.classList.remove('fade-image'); 
        activeImage.classList.remove('active'); 
      }
      backgroundOverlay.style.display = 'none';
    }
  });
});