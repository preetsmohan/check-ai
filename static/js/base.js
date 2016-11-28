$( document ).ready(function() {
    $(".button-collapse").sideNav();
});


function hideall(){
	$('.content-div').hide();
	document.body.innerHTML += "<div style='display:flex;justify-content:center;align-items:center;'><div class='loader center'></div>"

}
