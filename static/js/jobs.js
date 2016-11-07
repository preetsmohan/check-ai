$( document ).ready(function() {
    $('h6').each(function(index){
        $(this).html(utf8.decode($(this).html()));
    }
    );

});