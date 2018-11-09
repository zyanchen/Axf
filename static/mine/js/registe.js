$(function () {
    $('.register').width(innerWidth)
    $('#account input').blur(function () {
        if ($(this).val() == '') return
        var reg = /^[A-Za-z0-9]+$/
        if (reg.test($(this).val())) {
            console.log('aaa')
            $.get('/checkaccount/', {'account': $(this).val()}, function (response) {
                console.log(response)
                if (response.status == 1) {
                    $('#account i').html('')
                    $('#account').removeClass('has-error').addClass('has-success')
                    $('#account span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
                } else {
                    $('#account i').html(response.msg)
                    $('#account').removeClass('has-success').addClass('has-error')
                    $('#account span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
                }
            })
        } else {
            $('#account i').html('账号由数字、字母组成')
            $('#account').removeClass('has-success').addClass('has-error')
            $('#account span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })


    $('#password input').blur(function () {
        if ($(this).val() == '') return
        var reg = /^[a-z0-9]{6,12}$/
        if (reg.test($(this).val())) {
            $('#password i').html('')
            $('#password').removeClass('has-error').addClass('has-success')
            $('#password span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
        } else {
            $('#password i').html('密码由6~12位数字、字母组成')
            $('#password').removeClass('has-success').addClass('has-error')
            $('#password span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })

    $('#passwd input').blur(function () {
        if ($(this).val() == '') return

        if ($(this).val() == $('#password input').val()) {
            $('#passwd i').html('')
            $('#passwd').removeClass('has-error').addClass('has-success')
            $('#passwd span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
        } else {
            $('#passwd i').html('两次密码不一致')
            $('#passwd').removeClass('has-success').addClass('has-error')
            $('#passwd span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })


    $('#name input').blur(function () {
        if ($(this).val() == '') return
        $('#name').removeClass('has-error').addClass('has-success')
        $('#name span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
    })


    $('#tel input').blur(function () {
        if ($(this).val() == '') return
        var reg = /^1[3|5|7|8|]\d{9}$/
        if (reg.test($(this).val())) {
            $('#tel i').html('')
            $('#tel').removeClass('has-error').addClass('has-success')
            $('#tel span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
        } else {
            $('#tel i').html('请输入正确的手机号')
            $('#tel').removeClass('has-success').addClass('has-error')
            $('#tel span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })


    $('#addr input').blur(function () {
        if ($(this).val() == '') return
        $('#addr').removeClass('has-error').addClass('has-success')
        $('#addr span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
    })
})