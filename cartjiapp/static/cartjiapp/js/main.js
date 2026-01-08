
function changeImage(imageUrl) {
    document.getElementById('mainProductImage').src = imageUrl;
}



// hero section start

document.addEventListener("DOMContentLoaded", () => {
    const track = document.getElementById("heroTrack");
    const slides = document.querySelectorAll(".hero-slide");
    const dotsContainer = document.getElementById("heroDots");

    let index = 0;

    slides.forEach((_, i) => {
        const dot = document.createElement("span");
        if (i === 0) dot.classList.add("active");
        dot.onclick = () => moveSlide(i);
        dotsContainer.appendChild(dot);
    });

    const dots = dotsContainer.querySelectorAll("span");

    function moveSlide(i) {
        index = i;
        track.style.transform = `translateX(-${index * 100}%)`;
        dots.forEach(d => d.classList.remove("active"));
        dots[index].classList.add("active");
    }

    setInterval(() => {
        index = (index + 1) % slides.length;
        moveSlide(index);
    }, 4000);
});

// hero section end

document.addEventListener("DOMContentLoaded", function () {
    const reviewCards = document.querySelectorAll(".image-review-card");
    const modalImage = document.getElementById("reviewModalImage");

    reviewCards.forEach(card => {
        card.addEventListener("click", () => {
            const imgSrc = card.getAttribute("data-image");
            modalImage.src = imgSrc;
        });
    });
});


function changeProductImage(el) {
    document.getElementById("mainProductImage").src = el.src;
}
let selectedSize = "";
let selectedColor = "";

function selectSize(size, el) {
    selectedSize = size;
    document.querySelectorAll(".size-btn")
        .forEach(btn => btn.classList.remove("active"));
    el.classList.add("active");
    hideVariantMessage();
}

function selectColor(color, image, el) {
    selectedColor = color;
    document.getElementById("mainProductImage").src = image;

    document.querySelectorAll(".color-circle")
        .forEach(c => c.classList.remove("active"));
    el.classList.add("active");
    hideVariantMessage();
}

function orderOnWhatsApp(productName, price, productUrl) {
    if (!selectedSize && !selectedColor) {
        showVariantMessage("Please select size and color");
        return;
    }

    if (!selectedSize) {
        showVariantMessage("Please select a size");
        return;
    }

    if (!selectedColor) {
        showVariantMessage("Please select a color");
        return;
    }

    let message =
        `Hi, I want to order this product :\n\n` +
        `Product: ${productName}\n` +
        `Price: ₹${price}\n` +
        `Size: ${selectedSize}\n` +
        `Color: ${selectedColor}\n` +
        `Link: ${productUrl}`;

    const url = `https://wa.me/918303278845?text=${encodeURIComponent(message)}`;
    window.open(url, "_blank");
}


function showVariantMessage(text) {
    const el = document.getElementById("variantMessage");
    el.innerText = text;
    el.style.display = "block";
}

function hideVariantMessage() {
    const el = document.getElementById("variantMessage");
    el.style.display = "none";
}
