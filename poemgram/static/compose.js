
$( function() {
	let canBreak=false;
	let input = $( "#hidden" );
	$( "#sortable1, #sortable2" ).sortable({
		connectWith: ".connectedSortable"
    }).disableSelection();
	$( "#sortable1" ).sortable({
		items: "li:not(.anchor)"
    });
	$( "#sortable2" ).sortable({
		items: ["li:not(.wordcard)", "li:not(.break)"],
		receive: function( event, ui ) {
			input.val( input.val() + ui.item.text()+" " );
			canBreak=true;
			
		},
    });
	$(document).on('keypress',function(e) {
    if(e.which == 13) {
		$( "#sortable2" ).append("<li class=\"break\"/>");
		if(canBreak==true) {
			canBreak=false;
			input.val( input.val() +"\n" );
		}
    }});
	
} );

/*
$( function() {
    $( ".wordcard" ).draggable();
    $( "#droppable" ).droppable({
      drop: function( event, ui ) {
        $( this )
          .addClass( "ui-state-highlight" )
          .find( "p" )
            .html( "Dropped!" );
      }
    });
  } );*/