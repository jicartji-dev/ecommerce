
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
let selectedSize = null;
let selectedColor = null;

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

function showVariantMessage(text) {
    const el = document.getElementById("variantMessage");
    el.innerText = text;
    el.style.display = "block";
}

function hideVariantMessage() {
    const el = document.getElementById("variantMessage");
    el.style.display = "none";
}





// function orderOnWhatsApp(name, price, url) {
//     if (selectedColor === "Not selected" || selectedSize === "Not selected") {
//         document.getElementById("variantMessage").innerText =
//             "⚠ Please select color and size before ordering";
//         return;
//     }
//     let coupon = document.getElementById("couponCode").value;
//     let finalPrice = parseFloat(price);

//     if (coupon.trim() === "") {
//         openWhatsApp(name, finalPrice, url);
//         return;
//     }

//     fetch(`/check-coupon/?code=${coupon}`)
//         .then(res => res.json())
//         .then(data => {

//             let modal = new bootstrap.Modal(document.getElementById('couponModal'));

//             if (data.valid) {
//                 let discountAmount = (finalPrice * data.discount) / 100;
//                 let discountedPrice = finalPrice - discountAmount;

//                 document.getElementById("modalTitle").innerText = "Coupon Applied 🎉";
//                 document.getElementById("modalDetails").innerHTML = `
//     <strong>${name}</strong><br>
//         Original Price: ₹${finalPrice}<br>
//             Discount: ₹${discountAmount}<br>
//                 <strong>Final Price: ₹${discountedPrice}</strong>
//                 `;

//                 document.getElementById("finalOrderBtn").onclick = function () {
//                     openWhatsApp(name, discountedPrice, url, coupon);
//                 };

//             } else {
//                 document.getElementById("modalTitle").innerText = "Invalid Coupon ❌";
//                 document.getElementById("modalDetails").innerHTML = `
//                 Coupon <strong>${coupon}</strong> is not valid.<br>
//                     Continue without discount?
//                     `;

//                 document.getElementById("finalOrderBtn").onclick = function () {
//                     openWhatsApp(name, finalPrice, url);
//                 };
//             }

//             modal.show();
//         });
// }


function orderOnWhatsApp(name, price, url) {

    // ✅ HARD STOP if variant not selected
    if (!selectedSize || !selectedColor) {
        showVariantMessage("⚠ Please select size and color before ordering");
        return;
    }

    let couponInput = document.getElementById("couponCode");
    let coupon = couponInput ? couponInput.value.trim() : "";

    let basePrice = parseFloat(price);
    if (isNaN(basePrice)) {
        alert("Price error. Please refresh page.");
        return;
    }

    // ✅ No coupon → direct WhatsApp
    if (coupon === "") {
        openWhatsApp(name, basePrice.toFixed(2), url);
        return;
    }

    // ✅ Coupon check
    fetch(`/check-coupon/?code=${encodeURIComponent(coupon)}`)
        .then(res => res.json())
        .then(data => {

            let modal = new bootstrap.Modal(
                document.getElementById('couponModal')
            );

            if (data.valid === true) {

                let discountAmount =
                    (basePrice * data.discount) / 100;

                let discountedPrice =
                    (basePrice - discountAmount).toFixed(2);

                document.getElementById("modalTitle").innerText =
                    "Coupon Applied 🎉";

                document.getElementById("modalDetails").innerHTML = `
<strong>${name}</strong><br>
Original Price: ₹${basePrice}<br>
Discount: ₹${discountAmount.toFixed(2)}<br>
<strong>Final Price: ₹${discountedPrice}</strong>
                `;

                document.getElementById("finalOrderBtn").onclick = function () {
                    openWhatsApp(name, discountedPrice, url, coupon);
                };

            } else {

                document.getElementById("modalTitle").innerText =
                    "Invalid Coupon ❌";

                document.getElementById("modalDetails").innerHTML = `
Coupon <strong>${coupon}</strong> is not valid.<br>
Continue without discount?
                `;

                document.getElementById("finalOrderBtn").onclick = function () {
                    openWhatsApp(name, basePrice.toFixed(2), url);
                };
            }

            modal.show();
        });
}


function openWhatsApp(name, price, url, coupon = "") {

    let message =
        `I want to order this product:

Product: ${name}
Price: ₹${price}
Size: ${selectedSize}
Color: ${selectedColor}
${coupon ? "Coupon: " + coupon + "\n" : ""}Link: ${url}`;

    window.open(
        `https://wa.me/918303278845?text=${encodeURIComponent(message)}`,
        "_blank"
    );
}
