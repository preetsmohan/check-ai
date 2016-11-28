function deletePref(objectId){
    $("#"+objectId).remove();
    $("#"+objectId+"-label").remove();
}

$( document ).ready(function() {

    // console.log();
    setRadioSelection($("#explevels").attr('data'));
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

