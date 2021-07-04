$(document).on('ready', function(){
    $('.gallery ul li a').click(function () {
        var itemID = $(this).attr('href');
        var url = $(this).attr('data-url');
        $('.gallery ul').addClass('item_open');
        $('.port img').attr('src', url)
        $(itemID).addClass('item_open');
        $('header').addClass('hide-header')
        return false;
    });
    $('.close').click(function () {
        $('.port, .gallery ul').removeClass('item_open');
        $('header').removeClass('hide-header')
        return false;
    });

    $(".gallery ul li a").click(function () {
        $('html, body').animate({
            scrollTop: parseInt($("#top").offset().top)
        }, 300);
    });
});