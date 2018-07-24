$('.btn').stop().on('click', function(){
	button = $(this);
	button.addClass('clicked');
	
	setTimeout(function(){
		button.addClass('success');
	},300);
	
	
	setTimeout(function(){
		button.removeClass('clicked');
		button.removeClass('success');
	},4000);
});