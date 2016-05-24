
	$(function(){
  $("#header a").click(function(){
    $("#header a").removeClass("selected")
    $(this).addClass("selected")
    return false;
  })
});

$(window).scroll(function() {
		$('#one').each(function(){
		var imagePos = $(this).offset().top;

		var topOfWindow = $(window).scrollTop();
			if (imagePos < topOfWindow+350) {
				$(this).addClass("slideUp");
			}
		});
		$('#two').each(function(){
		var imagePos = $(this).offset().top;

		var topOfWindow = $(window).scrollTop();
			if (imagePos < topOfWindow+300) {
				$(this).addClass("slideUp");
			}
		});
		$('#three').each(function(){
		var imagePos = $(this).offset().top;

		var topOfWindow = $(window).scrollTop();
			if (imagePos < topOfWindow+350) {
				$(this).addClass("slideUp");
			}
		});
	});