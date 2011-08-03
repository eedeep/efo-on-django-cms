// Implements html5 placeholder for non-supporting browsers.  req jQuery.
$(document).ready(function(){
    $("input").each(function(){
        if($(this).val()=="" && $(this).attr("placeholder")){
            $(this).val($(this).attr("placeholder"));
            var defaultColor = $(this).css('color');
            $(this).css({'color':'#D8172C'});
            $(this).focus(function(){
                if($(this).val()==$(this).attr("placeholder")){
                    $(this).val("");
                    $(this).css({'color':defaultColor});
                } 
            });
            $(this).blur(function(){
                if($(this).val()==""){
                    $(this).val($(this).attr("placeholder"));
                    $(this).css({'color':'#D8172C'});
                }
            });
        }
    });
});