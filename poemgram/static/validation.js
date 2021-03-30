var thisScript = document.currentScript;


jQuery.validator.addMethod("validEmail", function(value, element) 
{
	const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(value).toLowerCase());
},"Please enter a valid email address");

jQuery.validator.addMethod("validUsername", function(value, element) 
{
    return  /^(\w|\.|\+|-|@)*$/.test(String(value));
}, "Letters, digits and @/./+/-/_ only.");

jQuery.validator.addMethod("validPassword", function(value, element) 
{
    return  /\D/.test(String(value));
}, "Password must contain at least one non-numeric character");




$().ready(function()
{
	$("#regForm").validate(
	{
		rules:
		{
			username:
			{
				required: true,
				validUsername: true,
				// This is not very useful as the input already limits it to 150 chars, but I guess it's more compatible like this
				maxlength: 150, 
				remote: thisScript.getAttribute('validationUrl')
			},
			email:
			{
				required: true,
				validEmail: true,
			},
			
			password1:
			{
				required: true,
				minlength: 8,
				validPassword: true
				
			},
			
			password2:
			{
				required: true,
				equalTo: "#id_password1"
			}
		},
		messages:
		{
			username:
			{
				required: "Please enter an username.",
				validUsername: "Letters, digits and @/./+/-/_ only.",
				maxlength: "Please enter an username shorter that 150 characters.",
				remote: "Please enter a new username"
			}, 
			email:
			{
				required: "Please enter an email address",
				validEmail: "Please enter a valid email address"
			},
			password1:
			{
				required: "Please enter a password longer than eight characters",
				minlength: "Please enter a password longer than eight characters",
				validPassword: "The password must include a non-numeric character"
				
			},
			
			password2:
			{
				required: "Please confrim your password",
				equalTo: "Please confrim your password"
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