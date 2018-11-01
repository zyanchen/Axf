$(function () {

    $('.home').width(innerWidth)

    new Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        slidesPerView: 1,
        paginationClickable: true,
        spaceBetween: 5,
        loop: true,
    autoplay: 2000,
    });

    new Swiper('#mustbuySwiper', {
        slidesPerView: 3,
        spaceBetween: 10,
        loop: true,
    });
})