$(document).ready(function () {
    console.log("base.js loaded");
    console.log("faq items:", $(".faq-reveal").length);

    /* Header scroll styling */
    function toggleScrolledHeader() {
        var $header = $("header");

        if ($("body").hasClass("hero-page")) {
            if ($(window).scrollTop() > 20) {
                $header.addClass("header-scrolled");
            } else {
                $header.removeClass("header-scrolled");
            }
        } else {
            $header.addClass("header-scrolled");
        }
    }

    /* FAQ scroll reveal */
    function revealFaqSections() {
        $(".faq-reveal").each(function () {
            var elementTop = this.getBoundingClientRect().top;
            var windowHeight = window.innerHeight;

            if (elementTop < windowHeight - 60) {
                $(this).addClass("faq-reveal-visible");
            }
        });
    }

    /* Toasts and back to top */
    $(".toast").toast("show");

    $(".btt-link").click(function (e) {
        e.preventDefault();
        $("html, body").animate({
            scrollTop: 0
        }, 300);
    });

    /* FAQ page setup */
    if ($(".faq-reveal").length) {
        $(".faq-reveal").each(function () {
            $(this).addClass("faq-reveal-ready");
        });

        revealFaqSections();

        $(window).on("scroll", function () {
            revealFaqSections();
        });
    }

    /* Run header logic on load and scroll */
    toggleScrolledHeader();

    $(window).on("scroll", function () {
        toggleScrolledHeader();
    });
});