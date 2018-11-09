$(function () {
    $('.market').width(innerWidth)
    typeIndex = $.cookie('typeIndex')
    if (typeIndex){
        $('.type-slider .type-item').eq(typeIndex).addClass('active')
    }else {
        $('.type-slider .type-item').addClass('active')
    }
    $('.type-item').click(function () {
        // $(this).addClass('active')
        $.cookie('typeIndex', $(this).index(),{expires:3,path:'/'})
    })

    categoryBt = false
    $('#categoryBt').click(function () {
        categoryBt = !categoryBt
        categoryBt ? categoryShow() : categoryHide()
    })

    sortBt = false
    $('#sortBt').click(function () {
        sortBt = !sortBt
        sortBt ? sortShow() : sortHide()
    })

    $('.bounce-view').click(function () {
        sortBt = false
        sortHide()
        categoryBt = false
        categoryHide()
    })

    function categoryShow(){
        sortHide()
        sortBt = !sortBt
        $('.bounce-view.category-view').show()
        $('#categoryBt i').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
    }

    function categoryHide(){
        $('.bounce-view.category-view').hide()
            $('#categoryBt i').removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')
    }

    function sortShow(){
        categoryHide()
        categoryBt = !categoryBt
        $('.bounce-view.sort-view').show()
        $('#sortBt i').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
    }

    function sortHide(){
        $('.bounce-view.sort-view').hide()
        $('#sortBt i').removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')
    }



    $('.bt-wrapper .glyphicon-minus').hide()
    $('.bt-wrapper .num').hide()

    $('.bt-wrapper .num').each(function () {
        var num = parseInt($(this).html())
        if (num){
            $(this).show()
            $(this).prev().show()
        }
    })

    $('.bt-wrapper .glyphicon-plus').click(function () {
        var goodsid = $(this).attr('goodsid')
        var $that = $(this)
        $.get('/addcart/',{'goodsid':goodsid}, function (response) {
            console.log(response)
            if (response.status == -1){
                window.open('/login/', target="_self")
            } else if (response.status == 1){
                $that.prev().html(response.number).show()
                $that.prev().prev().show()
                console.log(response.number)
            }
        })
    })


    $('.bt-wrapper .glyphicon-minus').click(function () {
        var goodsid = $(this).attr('goodsid')
        var $that = $(this)
        $.get('/subcart/', {'goodsid':goodsid},function (response) {
            console.log(response)
            if (response.status == 1){
                var number = response.number
                if (number > 0) {
                    $that.next().html(number)
                }  else {
                    $that.next().hide()
                    $that.hide()
                }
            }
        })
    })


})