$(document).ready(function () {
    function toggleScrolledHeader() {
        var $header = $('header');

        if ($('body').hasClass('hero-page')) {
            if ($(window).scrollTop() > 20) {
                $header.addClass('header-scrolled');
            } else {
                $header.removeClass('header-scrolled');
            }
        } else {
            $header.addClass('header-scrolled');
        }
    }

    $('.toast').toast('show');

    $('.btt-link').click(function (e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: 0
        }, 300);
    });

    toggleScrolledHeader();

    $(window).on('scroll', function () {
        toggleScrolledHeader();
    });
});