$(document).on('ready', function(){
    $('.gallery ul li a').click(function () {
        var itemID = $(this).attr('href');
        var url = $(this).attr('data-url');
        var name = $(this).attr('data-name');
        var date = $(this).attr('data-details')
        var desc = $(this).attr('data-description')
        $('#pic h1').text(name)
        $('#pic p.details strong').text(date)
        $('#pic p.desc').text(desc)
        $('.gallery ul').addClass('item_open');
        $('.port img').attr('src', url)
        $('.port img').attr('alt', name)
        $(itemID).addClass('item_open');
        $('header').addClass('hide-header')

        $('.copy i').on('click', copyFunction(url))
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

    copyFunction = (url) => {
        const elem = document.createElement('input');
        elem.value = url;
        document.body.appendChild(elem);
        elem.select();
        document.execCommand('copy');
        document.body.removeChild(elem);
    }
});