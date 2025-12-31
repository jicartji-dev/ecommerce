
function changeImage(imageUrl) {
    document.getElementById('mainProductImage').src = imageUrl;
}



// hero section start

document.addEventListener("DOMContentLoaded", function () {

    const track = document.getElementById("carouselTrack");
    const slides = document.querySelectorAll(".hero-slide");
    const dotsContainer = document.getElementById("carouselDots");

    if (!track || slides.length === 0) return;

    let index = 0;

    slides.forEach((_, i) => {
        const dot = document.createElement("span");
        if (i === 0) dot.classList.add("active");
        dot.addEventListener("click", () => moveSlide(i));
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
    }, 3500);
});

// hero section end