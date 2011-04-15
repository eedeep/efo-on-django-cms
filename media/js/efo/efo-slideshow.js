$(document).ready(function() {
		
  var $ht = $('#slideshow-images:first-child').height();
  //$('#slideshow-images').css({height: $ht});

  $('#slideshow-images').cycle(
	{ 
		fx: 'fade',
		//slideResize : 0,
		after : function(currSlideElement, nextSlideElement, options, forwardFlag){
			var $ht = $(this).height();
		 	//$(this).parent().css({height: $ht});
		}
	}
  );
  $('#slideshow-images').cycle('pause');
  
  $('.object-slideshow-next').click(function(e) {
    e.preventDefault();
    $('#slideshow-images').cycle('next');
    console.log(e + "going to next slideshow image");
  });
    
  $('.object-slideshow-previous').click(function(e) {
    e.preventDefault();
    $('#slideshow-images').cycle('prev');
    console.log(e + "going to previous slideshow image");
  });
  
});
