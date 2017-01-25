$(document).ready(function () {	
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
		tmp = "{% url 'browse.filter_detail' '" + categories + "' '" + tags + "' %}"
		console.log(tmp);
		document.getElementById("custom-search-submit").href=tmp; 
    return false;
	});
});