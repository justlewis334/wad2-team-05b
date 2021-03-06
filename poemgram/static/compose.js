
// Ladies and gentlemen, this is Javascript
// from https://www.w3schools.com/js/js_random.asp
function getRndInteger(min, max) {
  return Math.floor(Math.random() * (max - min) ) + min;
}
// Do it before anything else so it doesnt show (if I put it in ready, it shows for half a second)
$( function() {
	// not ignore the hidden inputs
	$.validator.setDefaults({ 
		ignore: [],
	});
	$( "#textArea" ).hide();
	$( "#fakeTitle" ).hide();
	let sortable1 = $( "#sortable1" );
	let sortable2= $( "#sortable2" );
	let canBreak=false;
	let input = $( "#textArea" );
	let childList = $("#sortable1 li");
	
	
	$( "#sortable1, #sortable2" ).sortable({
		connectWith: ".cardContainer"
    }).disableSelection();
	
	sortable1.sortable({
		items: "li:not(.anchor)"
    });
	
	sortable2.sortable({
		cancel: ".wordcard",
		items: ["li:not(.wordcard)", "li:not(.break)"],
		receive: function( event, ui ) {
			input.val( input.val() + ui.item.text()+" " );
			childList = $("#sortable1 li")
			canBreak=true;
			
		},
    });
	
	$(document).on('keypress',function(e) {
    if(e.which == 13) {
		if(canBreak==true) {
			sortable2.append("<li class=\"break\"/>");
			canBreak=false;
			input.val( input.val() +"\n" );
		}
    }});
	
	$("#br").click(function() {
	if(canBreak==true) {
		sortable2.append("<li class=\"break\"/>");
		canBreak=false;
		input.val( input.val() +"\n" );
	}});
	
	$("#submit").click(function() {
		$("#fakeTitle").show();
		$( "#dialog" ).dialog({
			resizable: false,
			height: "auto",
			buttons: {
				"Create": function() {
					$("#title").val($("#fakeTitle").val())
					if ($("#submitForm").valid()){
						$("#submitForm").submit()
					}
				},
				Cancel: function() {
					$( this ).dialog( "close" );
				}
			}
		});
    });
	
	$("#rnd").click(function () {
		// the first child is the helpbox
		if (childList.length>1){
			let ele = childList.eq(getRndInteger(1, childList.length)).detach()
			sortable2.append(ele);
			childList = $("#sortable1 li");			
			input.val( input.val() + ele[0].innerText +" " );
			canBreak=true;
		}
	});
	
	$("#submitForm").validate(
	{
		rules:
		{
			poem:
			{
				required: true,
				minlength: 100,
			},
			title:
			{
				required: true,
			},
		},
		messages:
		{
			poem:
			{
				required: "Please enter a longer poem (minimum 100 characters)",
				minlength: "Please enter a longer poem (minimum 100 characters)",
			},
			title:
			{
				required: "Please enter a title",
			},
		},
		errorElement: "div",
		errorPlacement: function ( error, element ) {
					
			error.addClass( ["alert", "alert-danger", "noMargin"] );
			error.insertAfter( $(".navbar")[0] );
			setTimeout(function(){ error.fadeOut() }, 2000);
		},	
	});
} );
