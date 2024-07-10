const progressCircle = document.querySelector(".autoplay-progress svg");
const progressContent = document.querySelector(".autoplay-progress span");
var swiper = new Swiper(".mySwiper", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
        delay: 2500, slidesPerView: 1,
        disableOnInteraction: false
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev"
    },
    on: {
        autoplayTimeLeft(s, time, progress) {
            progressCircle.style.setProperty("--progress", 1 - progress);
            progressContent.textContent = `${Math.ceil(time / 1000)}s`;
        }
    }
});

var swiper = new Swiper(".mySwipernew", {
    slidesPerView: 4,
    spaceBetween: 0,
    speed: 800,
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});

document.querySelectorAll('.swiper-slide').forEach(function (slide) {
    slide.addEventListener('click', function () {
        // Hide all content divs
        document.querySelectorAll('.bank-button-detail').forEach(function (detail) {
            detail.style.display = 'none';
        });

        // Show the clicked content div
        var target = this.getAttribute('data-target');
        var targetElement = document.querySelector('.' + target);
        if (targetElement) {
            targetElement.style.display = 'block';
        }

        document.querySelectorAll('.swiper-slide').forEach(function (slide) {
            slide.classList.remove('active');
        });

        // Add 'active' class to the clicked swiper slide
        this.classList.add('active');
    });
});


// font resizer
const initialSizes = {};

document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll('.font_resizer');
    elements.forEach(element => {
        initialSizes[element.className] = window.getComputedStyle(element).fontSize;
    });
});

function resizeText(action) {
    const elements = document.querySelectorAll('.font_resizer');

    if (elements.length === 0) {
        console.error('No elements found with the specified classes');
        return;
    }

    elements.forEach(element => {
        let currentSize = window.getComputedStyle(element).fontSize;
        let currentSizeValue = parseFloat(currentSize);
        let unit = currentSize.slice(-2); // Get the unit (px or em)

        if (action === 'increase') {
            element.style.fontSize = (currentSizeValue + 0.2) + unit;
        } else if (action === 'decrease') {
            element.style.fontSize = (currentSizeValue - 0.2) + unit;
        } else if (action === 'default') {
            element.style.fontSize = initialSizes[element.className]; // Reset to initial font size
        }
    });
}

// translations
function loadGoogleTranslate() {
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
    document.body.appendChild(script);
}

function googleTranslateElementInit() {
    new google.translate.TranslateElement({
        pageLanguage: 'en',
        includedLanguages: 'hi',
        layout: google.translate.TranslateElement.InlineLayout.SIMPLE
    }, 'google_element');
}

function resetTranslation() {
    location.reload();
}