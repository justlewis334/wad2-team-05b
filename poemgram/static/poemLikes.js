const thisScript = document.currentScript;

$('.like-form').submit(function(e){
    e.preventDefault()

    const poem_id = $(this).attr('id')

    const likeText = $('.like-button${poem_id}').text()
    const trim = $.trim(likeText)
    const url = $(this).attr('action')

    let res;
    const likes = $('.like-count${poem_id}').text()
    const trimCount = parseInt(likes)

    $.ajax({
        type: 'POST',
        url: url,
        data: {
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            'poem_id':poem_id,
        },
        success: function (response) {
            if(trim === 'Unlike') {
                $('.like-button${poem_id}').text('Like')
                res = trimCount - 1
            } else {
                $('.like-button${poem_id}').text('Unlike')
                res = trimCount + 1
            }
            $('.like-count${poem_id}').text(res)
        },
        error: function (error) {
            console.log(error);
            alert("An error occurred.");
        }
    })
})
