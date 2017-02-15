$(document).ready(function () {	
	$(".flipper").flip({
    	trigger: 'hover',
	});

	$(".custom-search-button").click(function(){
	    $("#custom-search-options").toggle();
	});

	$("#custom-search-submit").click(function() {
		categories = $('.category-option:checked').map(function() {
		    return this.value;
		}).get().join('&');
		tags =  $('.tag-option:checked').map(function() {
		    return this.value;
		}).get().join('&');
		tmp = "/browse/filter/category=" + categories + "/tags=" + tags + "/"
		console.log(tmp);
		window.location.href = tmp;
		// document.getElementById("custom-search-submit").href=tmp; 
    return tmp;
	});
});