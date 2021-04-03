var thisScript = document.currentScript;


$().ready(function()
{

	
	if (thisScript.getAttribute("badUrl")=="True")
	{
			var t = $("<div class='alert alert-danger alert-dismissible fade show' role='alert'>The url you entered was incompatible with our system, please try another url. <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>");
			t.insertAfter(".navbar");
	}
	
	// from https://stackoverflow.com/questions/37530690/jquery-validate-plugin-one-field-required-but-not-both
    $.validator.addMethod('onlyOne', function(value, element, param) {
        return this.optional(element) || $('[name="' + param[0] + '"]').is(':blank');
    }, "Please fill out only one of these fields");
	
	
	
	$("#textForm").validate(
	{
		rules:
		{
			url:
			{
				url: true,
				onlyOne: ["text"],
				require_from_group: [1, ".form-control"]
			},
			text:
			{
				onlyOne: ["url"],
				require_from_group: [1, ".form-control"],
				minlength: 130,
			},
			title:
			{
				onlyOne: ["url"],
			}
			
			
		},
		messages:
		{
			url:
			{
				url: "Please provide a valid URL",
				onlyOne: "Please only provide either a text and an article title or an url",
				require_from_group: "Please provide either a text or an url"
			},
			text:
			{
				onlyOne: "Please only provide either a text or an url",
				require_from_group: "Please provide either a text or an url",
				minlength: "Please input a longer article"
			},
			title:
			{
				onlyOne: "Please only provide either a text and an article title or an url",
			}
		},
		errorElement: "div",
		errorPlacement: function ( error, element ) {
					
			error.addClass( "invalid-feedback" );
			
			error.insertAfter( element );
		},		
		highlight: function ( element, errorClass, validClass ) 
		{
			$( element ).addClass( "is-invalid" ).removeClass( "is-valid" );
		},
		unhighlight: function (element, errorClass, validClass) 
		{
			$( element ).addClass( "is-valid" ).removeClass( "is-invalid" );
		}
	});

})