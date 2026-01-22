/* ===============================
   PRODUCT IMAGE CHANGE
================================ */
function changeImage(imageUrl) {
    const img = document.getElementById("mainProductImage");
    if (img) img.src = imageUrl;
}

function changeProductImage(el) {
    const img = document.getElementById("mainProductImage");
    if (img) img.src = el.src;
}



/* =====================================================
   HERO COVERFLOW SLIDER – HARD 3D
===================================================== */

document.addEventListener("DOMContentLoaded", () => {
    const track = document.querySelector(".hero-visual-track");
    const slides = Array.from(document.querySelectorAll(".hero-visual-track img"));

    if (!track || slides.length === 0) return;

    let index = 0;
    const total = slides.length;
    const delay = 4000;

    function updateSlides() {
        slides.forEach((slide, i) => {
            slide.classList.remove("active", "prev", "next");

            if (i === index) {
                slide.classList.add("active");
            } else if (i === index - 1 || (index === 0 && i === total - 1)) {
                slide.classList.add("prev");
            } else if (i === index + 1 || (index === total - 1 && i === 0)) {
                slide.classList.add("next");
            }
        });

        track.style.transform = `translateX(-${index * 100}%)`;
    }

    function moveSlide() {
        index = (index + 1) % total;
        updateSlides();
    }

    updateSlides();
    setInterval(moveSlide, delay);
});



/* ===============================
   REVIEW IMAGE MODAL
================================ */
document.addEventListener("DOMContentLoaded", () => {
    const reviewCards = document.querySelectorAll(".image-review-card");
    const modalImage = document.getElementById("reviewModalImage");

    if (!modalImage) return;

    reviewCards.forEach(card => {
        card.addEventListener("click", () => {
            const imgSrc = card.getAttribute("data-image");
            modalImage.src = imgSrc;
        });
    });
});


/* ===============================
   PRODUCT VARIANT SELECTION
================================ */



function selectSize(size, btn) {
    selectedSize = size;
    document.querySelectorAll(".size-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");

    document.getElementById("variantMessage").style.display = "none";
}

function selectColor(color, imageUrl, el) {
    selectedColor = color;
    document.getElementById("mainProductImage").src = imageUrl;
    document.querySelectorAll(".color-circle").forEach(c => c.classList.remove("active"));
    el.classList.add("active");

    document.getElementById("variantMessage").style.display = "none";
}
