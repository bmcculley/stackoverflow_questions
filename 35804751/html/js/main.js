$(document).ready( function() {
	console.log('ready captain');
	setTimeout(addContent, 15000);
});

function addContent() {
	$('.content').append('<p>This conent is loaded by ajax after the page has been sitting a while.');
}