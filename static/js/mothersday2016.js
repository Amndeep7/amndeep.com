function fill_background() {
	let text = '';
	for(let i = 0; i < 5000; i++) {
		text += "HAPPY MOTHER'S DAY ";
	}
	$('#backgroundtext').html('<p>' + text + '</p>');
}	
