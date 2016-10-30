var password, confirmPassword, match, submit, name;

$( document ).ready(function() {
    var interval = 100;
    submit = $("#submit-button");
    //check password every 100ms
    setInterval(passwordCheck, interval);
});

function passwordCheck() {
    password = $('#password').val();
    confirmPassword = $("#confirm-password").val();
    name = $('#full-name').val();
    blank = password == '' || confirmPassword == '' || name =='';
    if (blank || password != confirmPassword) {
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