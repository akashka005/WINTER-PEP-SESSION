document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
            const navMenu = document.querySelector('.nav-menu');
            if (navMenu && navMenu.style.display === 'flex') {
                navMenu.style.display = 'none';
            }
        }
    });
});

const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

function closeNavMenu() {
    if (!navMenu) return;
    navMenu.classList.remove('open');
    hamburger?.classList.remove('active');
}

function openNavMenu() {
    if (!navMenu) return;
    navMenu.classList.add('open');
    hamburger?.classList.add('active');
}

if (hamburger && navMenu) {
    hamburger.addEventListener('click', (e) => {
        e.stopPropagation();
        if (navMenu.classList.contains('open')) {
            closeNavMenu();
        } else {
            openNavMenu();
        }
    });
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth < 992) closeNavMenu();
        });
    });
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.nav-wrapper') && window.innerWidth < 992) {
            closeNavMenu();
        }
    });
    window.addEventListener('resize', debounce(() => {
        if (window.innerWidth >= 992) {
            navMenu.classList.remove('open');
            navMenu.style.display = '';
            hamburger.classList.remove('active');
        }
    }, 200));
}

const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeInUp 0.6s ease forwards';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.skill-category, .project-card, .metric-card, .contact-info-card').forEach(el => {
    el.style.opacity = '0';
    observer.observe(el);
});

let ticking = false;
window.addEventListener('scroll', () => {
    if (!ticking) {
        window.requestAnimationFrame(() => {
            const hero = document.querySelector('.hero-content');
            if (hero) {
                const scrolled = window.scrollY;
                hero.style.transform = `translateY(${scrolled * 0.5}px)`;
            }
            ticking = false;
        });
        ticking = true;
    }
});

document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-4px)';
        this.style.transition = 'all 0.3s ease';
    });

    btn.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
    });
});

window.addEventListener('resize', debounce(() => {
    if (window.innerWidth > 768 && navMenu && navMenu.style.display === 'flex') {
        navMenu.style.display = '';
        hamburger.classList.remove('active');
    }
}, 250));

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

document.addEventListener('DOMContentLoaded', () => {
    console.log('✨ Professional Portfolio Loaded & Ready!');
    document.body.classList.add('loaded');
    
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src || img.src;
                    imageObserver.unobserve(img);
                }
            });
        });
        document.querySelectorAll('img[data-src]').forEach(img => imageObserver.observe(img));
    }
});

window.addEventListener('error', (e) => {
    console.error('Portfolio Error:', e.error);
});