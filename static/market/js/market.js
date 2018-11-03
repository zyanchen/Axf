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

})