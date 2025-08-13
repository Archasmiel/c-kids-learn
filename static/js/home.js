document.addEventListener('DOMContentLoaded', function () {

    /* -------------------------------
       Smooth Scroll to Target
    -------------------------------- */
    document.querySelectorAll('.scroll-to').forEach(btn => {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            const selector = this.getAttribute('data-scroll-to');
            const target = document.querySelector(selector);
            if (target) {
                const topOffset = 56; // height of your navbar
                const elementPosition = target.getBoundingClientRect().top + window.pageYOffset;
                const offsetPosition = elementPosition - topOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    /* -------------------------------
       Random Button Colors in Carousel
    -------------------------------- */
    const colors = [
        "btn-success",
        "btn-danger",
        "btn-secondary"
    ];

    function randomColorClass() {
        return colors[Math.floor(Math.random() * colors.length)];
    }

    const carousel = document.getElementById('fullPageCarousel');

    function updateExploreButtons() {
        document.querySelectorAll('.carousel-item.active .btn-attractive').forEach(btn => {
            // Remove old Bootstrap color classes
            btn.classList.remove("btn-success", "btn-danger", "btn-secondary");
            // Add a random one
            btn.classList.add(randomColorClass());
        });
    }

    // Run on page load
    updateExploreButtons();

    // Run on carousel slide
    if (carousel) {
        carousel.addEventListener('slid.bs.carousel', function () {
            updateExploreButtons();
        });
    }

});
