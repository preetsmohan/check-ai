$( document ).ready(function() {
    $(".button-collapse").sideNav();
});


function hideall(){
	$('.content-div').hide();
	document.body.innerHTML += "<div class='loader'></div>"
}
