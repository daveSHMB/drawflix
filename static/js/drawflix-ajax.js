$(document).ready( function() {

	//when find film button clicked
	$('#submit_search').click(function(event){
		var searchFilm =  $("#film_search").val(); //value to search for is value in searchFilm box
		$.ajax({
			type: 'GET',
  url: 'http://www.omdbapi.com/?s=' + searchFilm,
  dataType: 'json',
  async: false, //wait for response before updating details
  success: function(json_data){
		$('#options option').remove(); //remove any previous options on the dropdown
		for (var i = 0; i < json_data.Search.length; i++) { //loop through JSON results and append to options
		$('#options').append('<option value="' + json_data.Search[i].Title + '">' + json_data.Search[i].Title + '</option>');
		}
		//hide form error if currently displayed
		$("#submit_error").hide();
		//unhide the options box if hidden(default)
		$("#options").show();
		//clear the search box for next input
		$("#film_search").val('');
		//auto selects first film in dropdown if first result of search is desired user response
		$("#id_film").val($("#options").val());
	}
		});
	});

});
