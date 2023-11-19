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
