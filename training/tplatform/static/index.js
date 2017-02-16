$(document).ready(function () {	
	// 
	$(".flipper").flip({
    	trigger: 'hover',
	});

	$(".custom-search-button").click(function(){
	    $("#custom-search-options").toggle();
	    $('.blurred').toggle();
	});
	$("#close-box").click(function(){
	    $("#custom-search-options").toggle();
	    $('.blurred').toggle();
	});

	$("#custom-search-submit").click(function() {
		categories = $('.category-option:checked').map(function() {
		    return this.value;
		}).get().join('&');
		tags =  $('.tag-option:checked').map(function() {
		    return this.value;
		}).get().join('&');
		types =  $('.type-option:checked').map(function() {
		    return this.value;
		}).get().join('&');
		authors =  $('.author-option:checked').map(function() {
		    return this.value;
		}).get().join('&');
		tmp = "/browse/filter/category=" + categories + "/tags=" + tags + "/types=" + types + "/authors=" + authors + "/"
		// console.log(tmp);
		window.location.href = tmp;
		// document.getElementById("custom-search-submit").href=tmp; 
    return tmp;
	});	

	var fix = $('.scroll-then-fix')
  	$(document).scroll(function() {
		if ( $(this).scrollTop() >= 90 ){
			fix.addClass('fix-to-top')
		} 
		else {
			fix.removeClass('fix-to-top')
		}
	})

	var fixSidebar = $('.scroll-then-fix-sidebar')
  	$(document).scroll(function() {
		if ( $(this).scrollTop() >= 90 ) {
			fixSidebar.addClass('fix-to-top-sidebar')
		}
		else {
			fixSidebar.removeClass('fix-to-top-sidebar')
		}
	})
});