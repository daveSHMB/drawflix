$(document).ready( function() {

//adds selected film to hidden submission form
$("#options").on("change", function() {
      $("#id_film").val($(this).val());
    });



	//for likes ----------
	$(document).on("click","#like", function(){
		var catid;
		catid = $(this).attr("data-catid");
		$.get('/like_drawing/', {drawing_id: catid}, function(data){
			$('#' + catid).html(data);

    });
	

	$(this).attr("disabled", true);;

	});

//creates drawing board object
	var myBoard = new DrawingBoard.Board('test_board',{
	controls: [
		'Color',
		{ Size: { type: 'dropdown' } },
		{ DrawingMode: { filler: true } },
		'Navigation',
	],
	size: 1,
	webStorage: 'local',
	enlargeYourContainer: true
});

//when user submits drawing
	$("#finalise").click(function() {

		film = $("#id_film").val();
		//if film has been selected
		if(film != '') {

		var canvas = myBoard.getImg();

		$("#id_image").val(canvas);
		$('#confirm_drawing').click()
		$('.drawing-board-control-navigation-reset').click();
}
else { //if not, display error message
	$("#submit_error").fadeIn(500);
}

});

//fades in content
$("#fade_in").fadeIn(1000);

//highlights current page on navbar
$(function(){
  $('a').each(function() {
    if ($(this).prop('href') == window.location.href) {
      $(this).addClass('highlights');
    }
  });
});

});
