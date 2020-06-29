function toastMessage(tag, message) {
    titleTag = tag.charAt(0).toUpperCase() + tag.slice(1)
    $('.toast-wrapper').html(
                        `<div class="toast" data-delay="4000">
                            <div class="toast-header bg-${tag}"><strong class="mr-auto text-white">${titleTag}</strong><button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>
                            <div class="toast-body">${message}</div>
                        </div>`)
                    $('.toast').toast('show')
}

/**
 * Receives the like button press, prevents the page reload and runs the funxtion that
 * passes the info to Python.When it receives the data it swaps the icon on the heart 
 * to indicate liked/not liked.
 * @param {string} id - a unique id for that story which identifies the correct like button
 */
function buttonToggle(likedSvg, unlikedSvg, cartedSvg, uncartedSvg) {

    /**
     * Runs the form to like the post through an ajax function.
     */    
    function like(id, serializedData, formUrl, likedSvg, unlikedSvg) {
        // Sends form to flask view
        $.ajax({
            method: 'POST',
            url: formUrl,
            data: serializedData,
            datatype: 'json',
            success: function (data) {
                // If content is already liked, swaps the icon and plays the unlike sound on successful response
                if (data.content.result === 'liked') {
                //     var unlikeAudio = new Audio('/static/audio/pop-cork.wav');
                //     unlikeAudio.play();
                    $(`#like-svg-${id}`).attr('data', likedSvg);
                    $(`#like-img-${id}`).attr('src', likedSvg);
                    toastMessage(data.content.tag, data.content.message)
                }
                // Otherwise it likes it and plays the corresponding sound
                else if (data.content.result === 'unliked') {
                    // var likeAudio = new Audio('/static/audio/blop.wav');
                    // likeAudio.play();
                    $(`#like-svg-${id}`).attr('data', unlikedSvg);
                    $(`#like-img-${id}`).attr('src', unlikedSvg);
                    toastMessage(data.content.tag, data.content.message)
                }
                else if (data.content.result === 'carted') {
                    // var likeAudio = new Audio('/static/audio/blop.wav');
                    // likeAudio.play();
                    $(`#cart-svg-${id}`).attr('data', cartedSvg);
                    $(`#cart-img-${id}`).attr('src', cartedSvg);
                    toastMessage(data.content.tag, data.content.message)
                    if ($(`#btn-${id}`) != undefined) {
                        $(`#btn-${id}`).contents().last()[0].textContent='  Remove from Cart';
                    } 
                }
                else if (data.content.result === 'uncarted') {
                    // var likeAudio = new Audio('/static/audio/blop.wav');
                    // likeAudio.play();
                    $(`#cart-svg-${id}`).attr('data', uncartedSvg);
                    $(`#cart-img-${id}`).attr('src', uncartedSvg);
                    if ($(`#btn-${id}`) == null) {
                        $(`#btn-${id}`).contents().last()[0].textContent='  Add to Cart';
                    }
                    if (window.location.pathname == "/cart/") {
                        console.log(id)
                        $(`#cart-item-${id}`).fadeOut("slow")
                    }
                    toastMessage(data.content.tag, data.content.message)
                }
                else {
                    toastMessage(data.content.tag, data.content.message)
                }
            }
        });
    }
        $(`.toggle-form`).on('submit', function(ev) {
        // stops form from sending
        ev.preventDefault();
        var id = this.id.slice(3);
        console.log(id)
        var serializedData = $(this).serialize()
        var formUrl = this.action
        like(id, serializedData, formUrl, likedSvg, unlikedSvg, cartedSvg, uncartedSvg)
        })
}