let thisScript = document.currentScript;

$( function() {


	$(".like-button").click(function() {
		let submitButton=$(this);
		let obj_id = submitButton.attr("id");
		let type = submitButton.attr("name");
		let likeText = submitButton.text();
		$.ajax({
			type: 'POST',
			url: thisScript.getAttribute("url"),
			headers: {'X-CSRFToken': Cookies.get('csrftoken')},
			data: {
				'obj_id': obj_id,
				'type': type,
			},
			success: function (response) {
				res = response["likes"];
				submitButton.text(response["newStatus"])
				$("#"+obj_id+type+"0").text(res)
			},
			error: function (error) {
				console.log(error);
				alert("An error occurred.");
			}
    })})
})
