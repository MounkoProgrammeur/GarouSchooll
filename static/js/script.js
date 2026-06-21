document.addEventListener('DOMContentLoaded', function () {

    // ── ANIMATION AU SCROLL ──
    // On cible automatiquement les cartes et éléments de liste pour les faire
    // apparaitre en douceur quand ils entrent dans l'écran.
    const elementsAAnimer = document.querySelectorAll(
        '.main-content .card, .document-item, .notif-item'
    );

    elementsAAnimer.forEach((el, index) => {
        el.classList.add('reveal-on-scroll');
        // petit décalage progressif pour un effet "cascade"
        el.style.transitionDelay = (index % 8) * 0.05 + 's';
    });

    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

        elementsAAnimer.forEach(el => observer.observe(el));
    } else {
        // Navigateur trop ancien : on affiche directement sans animation
        elementsAAnimer.forEach(el => el.classList.add('is-visible'));
    }

    // ── GRAPHIQUE ──
    const canvas = document.getElementById('performanceChart');
    if (canvas) {
        const notes    = [18, 12, 19, 7, 10, 14.5];
        const matieres = ['Algorithmique', 'Programmation', 'Base de données', 'Structures de Donnés', 'Mathematiques', 'Réseaux'];

        function getCouleur(note) {
            if (note >= 14) return '#16A34A';
            if (note >= 10) return '#D97706';
            return '#F21212';
        }

        new Chart(canvas.getContext('2d'), {
            type: 'line',
            data: {
                labels: matieres,
                datasets: [{
                    data: notes,
                    borderColor: '#9CA3AF',
                    borderWidth: 2,
                    pointBackgroundColor: notes.map(getCouleur),
                    pointBorderColor: notes.map(getCouleur),
                    pointRadius: 10,
                    pointHoverRadius: 12,
                    tension: 0.3,
                    fill: false
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: {
                    x: {
                        title: { display: true, text: 'Matière', font: { weight: 'bold', size: 14 } },
                        ticks: { maxRotation: 45, minRotation: 45 },
                        grid: { display: false }
                    },
                    y: {
                        title: { display: true, text: 'Notes /20', font: { weight: 'bold', size: 14 } },
                        min: 0, max: 20,
                        ticks: { stepSize: 5 },
                        grid: { color: '#E5E7EB' }
                    }
                }
            }
        });
    }

    // ── MORATOIRE ──
    const zoneUpload       = document.getElementById('zoneUpload');
    const montantMoratoire = document.getElementById('montantMoratoire');

    // Si ces éléments n'existent pas sur la page → on arrête
    if (!zoneUpload || !montantMoratoire) return;

    const inputFichier  = document.getElementById('recu');
    const nomFichier    = document.getElementById('nomFichier');
    const apercu        = document.getElementById('apercu');
    const btnValider    = document.getElementById('btnValider');
    const btnChoisir    = document.getElementById('btnChoisir');
    const erreurMontant = document.getElementById('erreurMontant');

    let fichierValide = false;
    let montantValide = false;

    zoneUpload.addEventListener('click', () => inputFichier.click());

    btnChoisir.addEventListener('click', (e) => {
        e.stopPropagation();
        inputFichier.click();
    });

    zoneUpload.addEventListener('dragover', (e) => {
        e.preventDefault();
        zoneUpload.style.background  = '#EFF6FF';
        zoneUpload.style.borderColor = '#1E90FF';
    });

    zoneUpload.addEventListener('dragleave', () => {
        zoneUpload.style.background  = '';
        zoneUpload.style.borderColor = '';
    });

    zoneUpload.addEventListener('drop', (e) => {
        e.preventDefault();
        zoneUpload.style.background  = '';
        zoneUpload.style.borderColor = '';
        if (e.dataTransfer.files[0]) traiterFichier(e.dataTransfer.files[0]);
    });

    inputFichier.addEventListener('change', function () {
        if (this.files && this.files[0]) traiterFichier(this.files[0]);
    });

    function traiterFichier(fichier) {
        const formatsAcceptes = ['application/pdf', 'image/jpeg', 'image/png', 'image/svg+xml'];
        const tailleMax = 10 * 1024 * 1024;

        if (!formatsAcceptes.includes(fichier.type)) {
            nomFichier.innerHTML = '<span class="text-danger"><i class="bi bi-x-circle-fill"></i> Format non accepté.</span>';
            fichierValide = false;
            apercu.classList.add('d-none');
            verifierBouton();
            return;
        }

        if (fichier.size > tailleMax) {
            nomFichier.innerHTML = '<span class="text-danger"><i class="bi bi-x-circle-fill"></i> Fichier trop lourd. Maximum 10Mo.</span>';
            fichierValide = false;
            apercu.classList.add('d-none');
            verifierBouton();
            return;
        }

        const tailleMo = (fichier.size / (1024 * 1024)).toFixed(2);
        nomFichier.innerHTML = `<span class="text-success"><i class="bi bi-check-circle-fill"></i> ${fichier.name} (${tailleMo} Mo)</span>`;
        fichierValide = true;
        verifierBouton();

        if (fichier.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = (e) => {
                apercu.src = e.target.result;
                apercu.classList.remove('d-none');
            };
            reader.readAsDataURL(fichier);
        } else {
            apercu.classList.add('d-none');
        }
    }

    montantMoratoire.addEventListener('input', function () {
        const valeur = parseInt(this.value);
        if (valeur > 100000) {
            erreurMontant.classList.remove('d-none');
            montantValide = false;
        } else if (valeur > 0) {
            erreurMontant.classList.add('d-none');
            montantValide = true;
        } else {
            erreurMontant.classList.add('d-none');
            montantValide = false;
        }
        verifierBouton();
    });

    function verifierBouton() {
        btnValider.disabled = !(fichierValide && montantValide);
    }

    btnValider.addEventListener('click', function () {
        document.getElementById('modalIcone').textContent   = '⏳';
        document.getElementById('modalTitre').textContent   = 'Soumission en cours...';
        document.getElementById('modalMessage').textContent = 'Votre reçu est en cours de traitement.';
        document.getElementById('modalBtns').classList.add('d-none');

        const modal = new bootstrap.Modal(document.getElementById('modalConfirmation'));
        modal.show();

        setTimeout(() => {
            document.getElementById('modalIcone').textContent   = '✅';
            document.getElementById('modalTitre').textContent   = 'Soumission réussie !';
            document.getElementById('modalMessage').textContent = 'Votre reçu a été soumis. En attente de vérification.';
            document.getElementById('modalBtns').classList.remove('d-none');
        }, 2000);
    });

});

// ── DOCUMENTS ──
    const rechercheDoc = document.getElementById('rechercheDoc');
    const triDoc       = document.getElementById('triDoc');

    if (rechercheDoc) {
        rechercheDoc.addEventListener('input', function () {
            const terme = this.value.toLowerCase();
            const docs  = document.querySelectorAll('.document-item');
            let aucun   = true;

            docs.forEach(doc => {
                const nom = doc.dataset.nom.toLowerCase();
                if (nom.includes(terme)) {
                    doc.classList.remove('d-none');
                    aucun = false;
                } else {
                    doc.classList.add('d-none');
                }
            });

            document.getElementById('aucunResultat').classList.toggle('d-none', !aucun);
        });
    }

    if (triDoc) {
        triDoc.addEventListener('change', function () {
            const liste  = document.getElementById('listeDocuments');
            const docs   = [...liste.querySelectorAll('.document-item')];

            docs.sort((a, b) => {
                if (this.value === 'nom') {
                    return a.dataset.nom.localeCompare(b.dataset.nom);
                }
                if (this.value === 'ancien') {
                    return a.dataset.date - b.dataset.date;
                }
                return b.dataset.date - a.dataset.date; // recent
            });

            docs.forEach(doc => liste.appendChild(doc));
        });
    }

// ── NOTIFICATIONS ──
    const filtres = document.querySelectorAll('.filtre-btn');
    if (filtres.length > 0) {
        filtres.forEach(btn => {
            btn.addEventListener('click', function () {
                filtres.forEach(b => b.classList.remove('btn-primary', 'active'));
                filtres.forEach(b => b.classList.add('btn-outline-secondary'));
                this.classList.remove('btn-outline-secondary');
                this.classList.add('btn-primary', 'active');

                const filtre = this.dataset.filtre;
                const notifs = document.querySelectorAll('.notif-item');
                let aucune = true;

                notifs.forEach(n => {
                    if (filtre === 'tout' || n.classList.contains(filtre)) {
                        n.classList.remove('d-none');
                        aucune = false;
                    } else {
                        n.classList.add('d-none');
                    }
                });

                document.getElementById('aucuneNotif').classList.toggle('d-none', !aucune);
            });
        });

        // Tout marquer comme lu
        const btnToutLire = document.getElementById('btnToutLire');
        if (btnToutLire) {
            btnToutLire.addEventListener('click', function () {
                document.querySelectorAll('.notif-item.non-lu').forEach(n => {
                    n.classList.remove('non-lu');
                    n.classList.add('lu');
                    n.querySelector('.badge').className = 'badge bg-success rounded-pill';
                    n.querySelector('.badge').textContent = 'Lu';
                });
            });
        }
    }

    // ── PARAMETRES - toggle mot de passe ──
    window.toggleMdp = function(id) {
        const input = document.getElementById(id);
        const icon  = document.getElementById('icon' + id.charAt(0).toUpperCase() + id.slice(1));
        if (input.type === 'password') {
            input.type = 'text';
            icon.className = 'bi bi-eye';
        } else {
            input.type = 'password';
            icon.className = 'bi bi-eye-slash';
        }
    };

    const btnChangerMdp = document.getElementById('btnChangerMdp');
    if (btnChangerMdp) {
        btnChangerMdp.addEventListener('click', function () {
            const mdpNew     = document.getElementById('mdpNew').value;
            const mdpConfirm = document.getElementById('mdpConfirm').value;
            const erreur     = document.getElementById('erreurMdp');

            if (mdpNew !== mdpConfirm) {
                erreur.classList.remove('d-none');
            } else {
                erreur.classList.add('d-none');
                alert('Mot de passe changé avec succès !');
            }
        });
    }



const navLinks = document.querySelectorAll('.links');

navLinks.forEach(link =>{
    if(link.href === window.location.href){
        link.classList.add('active');
    }
});
navLinks.forEach(link =>{
    link.addEventListener('click', function(){
        navLinks.forEach(l => l.classList.remove('active'));
        this.classList.add('active');
    });
});