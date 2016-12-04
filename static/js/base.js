$( document ).ready(function() {
    $(".button-collapse").sideNav();
    // $('.divLoading').hide();
});


function hideall(){
    // $('.content-div').hide();
     $(document.body).addClass("loading");
 //    $('.divLoading').addClass("show");
 //    $('.divLoading').show();
	// document.body.innerHTML += "<div style='display:flex;justify-content:center;align-items:center;'><div class='loader center'></div>"

}


function logout(){

    $.post('/logout');

}