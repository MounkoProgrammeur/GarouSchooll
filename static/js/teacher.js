const navLinks = document.querySelectorAll('.links');

navLinks.forEach(link => {
    // Comparer uniquement le chemin (/dashboard/, /cours/...) sans le domaine
    if (link.pathname && link.pathname === window.location.pathname) {
        link.classList.add('active');
    }
});