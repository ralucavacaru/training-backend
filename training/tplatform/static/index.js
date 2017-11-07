$(document).ready(function() {	

	// flipping UI boxes
	$(".flipper").flip({
    	trigger: 'manual',
	});
	function flipToggle(e) {
		$(e).flip('toggle');
	};

	// hoverIntent for UI boxes
	$(".flipper").hoverIntent(function () {
		$(this).flip('toggle');
	});

	// custom search
	$(".custom-search-button").click(function(){
	    $("#custom-search-options").toggle('fade');
	    // $('.blurred').toggle('fade');
	});
	$("#close-box").click(function(){
	    $("#custom-search-options").toggle('fade');
	    // $('.blurred').toggle('fade');
	});
	$(".blurred").click(function(){
	    $("#custom-search-options").toggle('fade');
	    // $('.blurred').toggle('fade');
	});

	// mobile menu
	$(".burger-icon").click(function(){
	    $(".mobile-menu").toggle('slide', {direction: 'right'});
	    $('.mob-menu-blurred').toggle('fade');
	});
	$(".mob-menu-blurred").click(function(){
	    $(".mobile-menu").toggle('slide', {direction: 'right'});
	    $('.mob-menu-blurred').toggle('fade');
	});
	$(".mobile-menu").on("swiperight",function(event){
  		$(".mobile-menu").toggle('slide', {direction: 'right'});
  		$(".mob-menu-blurred").toggle('fade');
	});

	// custom search URL build-up
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
		tmp = "/browse/filter/category=" + categories + "/tags=" + tags + "/types=" + types + "/authors=" + authors + "/";
		window.location.href = tmp;
    return tmp;
	});	

	// scroll-then-fix for navigation bar and sidebars
	var fix = $('.scroll-then-fix')
  	$(document).scroll(function() {
		if ( $(this).scrollTop() >= 115 ){
			fix.addClass('fix-to-top')
		} 
		else {
			fix.removeClass('fix-to-top')
		}
	})

	var fixSidebar = $('.scroll-then-fix-sidebar')
  	$(document).scroll(function() {
		if ( $(this).scrollTop() >= 115 ) {
			fixSidebar.addClass('fix-to-top-sidebar')
		}
		else {
			fixSidebar.removeClass('fix-to-top-sidebar')
		}
	})

	var fixFilters = $('.scroll-then-fix-filter')
  	$(document).scroll(function() {
		if ( $(this).scrollTop() >= 115 ) {
			fixFilters.addClass('fix-to-top-filter')
		}
		else {
			fixFilters.removeClass('fix-to-top-filter')
		}
	})

	var fixed = document.getElementById('custom-search-options');
	fixed.addEventListener('touchmove', function(e) {
	        e.preventDefault();
	}, false);
});

