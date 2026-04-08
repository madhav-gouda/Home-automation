// Scroll reveal animation
const reveals = document.querySelectorAll('.card, .service-category, .project-card, .contact-grid > *, .about-grid > *');

function checkReveal() {
    for (let el of reveals) {
        const windowHeight = window.innerHeight;
        const revealTop = el.getBoundingClientRect().top;
        const revealPoint = 150;
        
        if (revealTop < windowHeight - revealPoint) {
            el.classList.add('active');
        } else {
            el.classList.remove('active');
        }
    }
}

window.addEventListener('scroll', checkReveal);
window.addEventListener('load', checkReveal);

// Add reveal class to elements
reveals.forEach(el => el.classList.add('reveal'));
// Mobile menu toggle
const toggle = document.getElementById("menu-toggle");
const navLinks = document.querySelector(".nav-links");

if (toggle) {
    toggle.addEventListener("click", () => {
        navLinks.classList.toggle("active");
    });
}