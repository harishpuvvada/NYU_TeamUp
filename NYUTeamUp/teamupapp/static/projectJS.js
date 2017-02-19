$(document).ready(function () {
    var cw = $('.category-container').width();
    $('.category-container').css({'height':cw+'px'});
    window.onresize = function(event) {
        var cw = $('.category-container').width();
        $('.category-container').css({'height':cw+'px'});
    };
});
