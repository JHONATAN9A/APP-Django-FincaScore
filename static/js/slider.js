document.addEventListener("DOMContentLoaded", function () {
    const gallery = document.querySelector(".gallery");
    const prevBtn = document.querySelector(".prev-btn");
    const nextBtn = document.querySelector(".next-btn");

    let scrollAmount = 0;
    const cardWidth = 315; // Tamaño de una tarjeta con margen
    const visibleCards = 3;
    const scrollMax = (gallery.children.length - visibleCards) * cardWidth;

    nextBtn.addEventListener("click", () => {
        if (scrollAmount < scrollMax) {
            scrollAmount += cardWidth * visibleCards; // Avanza 3 tarjetas
            gallery.style.transform = `translateX(-${scrollAmount}px)`;
        }
    });

    prevBtn.addEventListener("click", () => {
        if (scrollAmount > 0) {
            scrollAmount -= cardWidth * visibleCards; // Retrocede 3 tarjetas
            gallery.style.transform = `translateX(-${scrollAmount}px)`;
        }
    });
});
