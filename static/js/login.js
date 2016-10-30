var password, submit, name;

$( document ).ready(function() {
    var interval = 100;
    submit = $("#submit-button");
    //check password every 100ms
    setInterval(loginCheck, interval);
});

function loginCheck() {
    password = $('#password').val();
    name = $('#full-name').val();
    blank = password == '' || name =='';
    if (blank) {
        //disable the submit button
        submit.addClass('disabled');
        submit.prop('disabled', true)
        console.log(submit.attr('class'));
    }
    else {
        submit.removeClass('disabled');
        submit.prop('disabled', false)
        console.log(submit.attr('class'));
    }
}