/**
 * Receives the like button press, prevents the page reload and runs the funxtion that
 * passes the info to Python.When it receives the data it swaps the icon on the heart 
 * to indicate liked/not liked.
 * @param {string} id - a unique id for that story which identifies the correct like button
 */

    /**
     * Runs the form to like the post through an ajax function.
     */    
    function likeUnlike(id, likeUrl) {
        // stops form from sending
        // Sends form to flask view
        $.ajax({
            method: 'POST',
            url: likeUrl,
            data: $(this).serialize(),
            datatype: 'json',
            success: function (data) {
                console.log("working")
                // // If content is already liked, swaps the icon and plays the unlike sound on successful response
                // if ($(`#heart-${id}`).text() === 'favorite') {
                //     var unlikeAudio = new Audio('/static/audio/pop-cork.wav');
                //     unlikeAudio.play();
                //     $(`#heart-${id}`).text('favorite_border');
                // }
                // // Otherwise it likes it and plays the corresponding sound
                // else {
                //     var likeAudio = new Audio('/static/audio/blop.wav');
                //     likeAudio.play();
                //     $(`#heart-${id}`).text('favorite');
                // }
            }
        });
    }
    // Waits for the like button press before firing off the function