function deletePref(objectId){
    $("#"+objectId).remove();
    $("#"+objectId+"-label").remove();
}
var moveFab;
$( document ).ready(function() {

    // console.log();
    setRadioSelection($("#explevels").attr('data'));
    moveFab = false;

    $(window).scroll(function() {
       if($(window).scrollTop() + $(window).height() == $(document).height()) {
        hideFab();
    }else{
        if(moveFab)
            showFab();
    }
});
});

function setRadioSelection(expLevel){
    switch(expLevel){
        case "Intern":
        $('#exp1').prop('checked', true);
        break;
        case "New Grad":
        $('#exp2').prop('checked', true);
        break;
        case "Entry Level":
        $('#exp3').prop('checked', true);
        break;
        case "Experienced":
        $('#exp4').prop('checked', true);
        break;
        case "Senior":
        $('#exp5').prop('checked', true);
        break;
        case "Executive":
        $('#exp6').prop('checked', true);
        break;
        default:
        $('#exp7').prop('checked', true);
        break;

    }
}

function hideFab(){
    $('#save-fab').animate({top: "150px"}, 100);
    moveFab = true;
    // $('#save-fab').hide();
}

function showFab(){
    $('#save-fab').animate({top: "0px"}, 100);
    moveFab = false;
    // $('#save-fab').show();
}
