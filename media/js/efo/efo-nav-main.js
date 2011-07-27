/* efo-nav-main.js 
   little bit of js to hide current page submenu items on menu hover */
   
$(document).ready(function(){
   efoHideDroplineSubmenus($('nav#main #dropline'));
});

function efoHideDroplineSubmenus(){
    var ancestor = $('nav#main #dropline li.ancestor');
    var selected = $('nav#main #dropline > li.selected');
    $('nav#main #dropline > li').hover(function(){
            ancestor.removeClass('ancestor');
            selected.removeClass('selected');
        }, function(){
            ancestor.addClass('ancestor');
            selected.addClass('selected');
    });
}
                                                                           