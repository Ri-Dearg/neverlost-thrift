function fadePreload() {
    $(".preloader").fadeOut(1200);
}

function hrefStop() {
    $(".href-stop").on("click", function (e) {
        e.preventDefault();
        return true;
    });
}

function toastMessage(tag, message) {
    var titleTag = tag.charAt(0).toUpperCase() + tag.slice(1);
    $(".toast-wrapper").html(
        `<div class="toast" data-delay="5000">
                            <div class="toast-header bg-${tag}"><strong class="mr-auto text-white">${titleTag}</strong><button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>
                            <div class="toast-body">${message}</div>
                        </div>`
    );
    $(".toast").toast("show");
}

/**
 * Receives the like button press, prevents the page reload and runs the funxtion that
 * passes the info to Python.When it receives the data it swaps the icon on the heart
 * to indicate liked/not liked.
 * @param {string} id - a unique id for that story which identifies the correct like button
 */
function buttonToggle(likedSvg, unlikedSvg, cartedSvg, uncartedSvg, likeUpdate, cartUpdate, cartRefresh) {
    function svgSwitch(btn, id, svgUrl) {
        $(`#${btn}-svg-${id}`).attr("data", svgUrl);
        $(`#${btn}-img-${id}`).attr("src", svgUrl);
    }

    function popoverUpdate(btn, update) {
        $(`#${btn}-popover`).popover("dispose");
        $(`#${btn}-popover-container`).fadeTo("fast", 0, function () {
            $(`#${btn}-popover-container`).html("").load(update);
            $(`#${btn}-popover-container`)
                .delay(400)
                .fadeTo("slow", 1, function () {
                    $(`#${btn}-popover`).popover();
                    $(".href-stop").off("click");
                    hrefStop();
                });
        });
    }

    /**
     * Runs the form to like the post through an ajax function.
     */
    function like(id, serializedData, formUrl) {
        // Sends form to flask view
        $.ajax({
            method: "POST",
            url: formUrl,
            data: serializedData,
            datatype: "json",
            success: function (data) {
                // If content is already liked, swaps the icon and plays the unlike sound on successful response
                if (data.content.result === "liked") {
                    svgSwitch("like", id, likedSvg);
                    toastMessage(data.content.tag, data.content.message);
                    popoverUpdate("like", likeUpdate);
                }
                // Otherwise it likes it and plays the corresponding sound
                else if (data.content.result === "unliked") {
                    svgSwitch("like", id, unlikedSvg);
                    toastMessage(data.content.tag, data.content.message);
                    popoverUpdate("like", likeUpdate);
                } else if (data.content.result === "carted") {
                    svgSwitch("cart", id, cartedSvg);
                    toastMessage(data.content.tag, data.content.message);
                    popoverUpdate("cart", cartUpdate);
                    if (data.content.special != "stocked") {
                        if ($(`#btn-${id}`).length > 0) {
                            $(`#btn-${id}`).contents().last()[0].textContent = "  Remove from Cart";
                        }
                    }
                } else if (data.content.result === "uncarted") {
                    svgSwitch("cart", id, uncartedSvg);
                    toastMessage(data.content.tag, data.content.message);
                    popoverUpdate("cart", cartUpdate);
                    if ($(`#btn-${id}`).length > 0) {
                        $(`#btn-${id}`).contents().last()[0].textContent = "  Add to Cart";
                    }
                    if (window.location.pathname == "/cart/") {
                        if (data.content.special != "update") {
                            $(`#cart-item-${id}`).fadeOut("slow");
                        }
                        $("#totals-box").fadeTo("slow", 0, function () {
                            $(`#totals-box`).html("").load(cartRefresh);
                            $(`#totals-box`).delay(400).fadeTo("slow", 1);
                        });
                    }
                } else {
                    toastMessage(data.content.tag, data.content.message);
                }
            },
        });
    }
    $(`.toggle-form`).on("submit", function (ev) {
        // stops form from sending
        ev.preventDefault();
        var id = this.id.slice(3);
        var serializedData = $(this).serialize();
        var formUrl = this.action;
        like(id, serializedData, formUrl);
    });
}
