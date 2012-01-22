$(document).ready(function(){
    $('#non-us-donation-form').css('display', 'none');
    $('#us-donation-form').css('display', 'none');

    $('input[name="donation-type"]').change(function(){
        if($(this).attr("id") == "non-us-donation-radio")
        {
            $('#non-us-donation-form').css('display', 'inline');
            $('#us-donation-form').css('display', 'none');
        }
        else
        {
            $('#non-us-donation-form').css('display', 'none');
            $('#us-donation-form').css('display', 'inline');
        }
    });
});
