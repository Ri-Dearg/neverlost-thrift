/**
 * Fades the preloader once content is loaded.
 */
function fadePreload() {
    $(".preloader").fadeOut(1200);
}

/**
 * Stops the page from jumping around when clicking on certain links, like the popover.
 */
function hrefStop() {
    $(".href-stop").on("click", function (e) {
        e.preventDefault();
        return true;
    });
}

/**
 * Creates a toast message after the parameters are passed from the Ajax function.
 * Is fired by the 'like' function.
 * @param {string} tag - Used as a header and a color class
 * @param {string} message - The message to display in the toast
 */
function toastMessage(tag, message) {
    // Cuts the tag so it can be used as text in the toast.
    var titleTag = tag.charAt(0).toUpperCase() + tag.slice(1);
    // Sets the toast HTML.
    $(".toast-wrapper").html(
        `<div class="toast" data-delay="5000">
                            <div class="toast-header bg-${tag}"><strong class="mr-auto text-white">${titleTag}</strong><button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>
                            <div class="toast-body">${message}</div>
                        </div>`
    );
    // Fires the toast.
    $(".toast").toast("show");
}

/**
 * Receives the like or cart button press, prevents the page reload and runs the function that
 * passes the info to a Python view.
 * On successful response, it receives the data it swaps the icon to indicate a button press.
 * It then deletes the popover content and fires another view which updates the popover templates and page context.
 * Animations are used throughout to smooth the experience.
 * @param {string} likedSvg - location of the SVG for a liked item.
 * @param {string} unlikedSvg - location of the SVG for an unliked item.
 * @param {string} cartedSvg - location of the SVG for a carted item.
 * @param {string} uncartedSvg - location of the SVG for an uncarted item.
 * @param {string} likeUpdate - url for the view that updates the like popover.
 * @param {string} cartUpdate - url for the view that updates the cart popover.
 * @param {string} cartRefresh - url for the view that updates the cart totals box on the cart_list page.
 */
function buttonToggle(likedSvg, unlikedSvg, cartedSvg, uncartedSvg, likeUpdate, cartUpdate, cartRefresh) {
    /**
     * Switches the SVG icons when a button is pressed.
     * @param {string} btn - Either 'cart' or 'like' depending on which button is pressed.
     * @param {string} id - The specific product id, so other products aren't selected.
     * @param {string} svgUrl - The URL for the SVG to use.
     */
    function svgSwitch(btn, id, svgUrl) {
        $(`#${btn}-svg-${id}`).attr("data", svgUrl);
        $(`#${btn}-img-${id}`).attr("src", svgUrl);
    }

    /**
     * First deletes the popover, then clears the popover html
     * and then fires the view that refreshes the template.
     * @param {string} btn - Either 'cart' or 'like' depending on which button is pressed.
     * @param {string} update - the URL which fires the view to update the template
     */
    function popoverUpdate(btn, update) {
        // Deletes the popover instance, necessary in bootstrap otherwise the new one won't load.
        $(`#${btn}-popover`).popover("dispose");
        // Animates the icon before deleting the HTML and loading the template refresh.
        $(`#${btn}-popover-container`).fadeTo("fast", 0, function () {
            $(`#${btn}-popover-container`).html("").load(update);
            // Animates the icon, then initialises the popover.
            $(`#${btn}-popover-container`)
                .delay(400)
                .fadeTo("slow", 1, function () {
                    $(`#${btn}-popover`).popover();
                    // Stops the page from jumping when clicking the icon.
                    $(".href-stop").off("click");
                    hrefStop();
                });
        });
    }

    /**
     * The main ajax function. Captures the form data and sends it to the the python view.
     * The response it receives is in JSON format.
     * On success it uses the different variables received in the response to perform logic
     * and decide which action to perform in a specific context.
     * @param {string} id - The specific product id, so other products aren't selected.
     * @param {string} serializedData - The data sent in POST form serialised.
     * @param {string} formUrl - The URL the data was being sent to.
     */
    function like(id, serializedData, formUrl) {
        // Sends form to Django view
        $.ajax({
            method: "POST",
            url: formUrl,
            data: serializedData,
            datatype: "json",
            success: function (data) {
                // If content is not liked, swaps the icon to the 'liked' icon
                // Sends off a message and refreshes the like popover.
                if (data.content.result === "liked") {
                    svgSwitch("like", id, likedSvg);
                    toastMessage(data.content.tag, data.content.message);
                    popoverUpdate("like", likeUpdate);

                // If content is already liked, swaps the icon to the 'unliked icon
                // Sends off a message and refreshes the like popover.
                } else if (data.content.result === "unliked") {
                    svgSwitch("like", id, unlikedSvg);
                    toastMessage(data.content.tag, data.content.message);
                    popoverUpdate("like", likeUpdate);

                // If content is not carted, swaps the icon to the 'carted' icon
                // Sends off a message and refreshes the cart popover.
                } else if (data.content.result === "carted") {
                    svgSwitch("cart", id, cartedSvg);
                    toastMessage(data.content.tag, data.content.message);
                    popoverUpdate("cart", cartUpdate);
                    // Used on the product_detail.html template.
                    // If the product does not have mutliple stock the button text switches.
                    if (data.content.special != "stocked") {
                        if ($(`#btn-${id}`).length > 0) {
                            $(`#btn-${id}`).contents().last()[0].textContent = "  Remove from Cart";
                        }
                    }

                // If content is already carted, swaps the icon to the 'uncarted' icon
                // Sends off a message and refreshes the cart popover.
                } else if (data.content.result === "uncarted") {
                    svgSwitch("cart", id, uncartedSvg);
                    toastMessage(data.content.tag, data.content.message);
                    popoverUpdate("cart", cartUpdate);

                    // Used on the product_detail.html template o change button text.
                    if ($(`#btn-${id}`).length > 0) {
                        $(`#btn-${id}`).contents().last()[0].textContent = "  Add to Cart";
                    }
                    //Used on the cart list page to remove items from view after being uncarted.
                    if (window.location.pathname == "/cart/") {
                        if (data.content.special != "update") {
                            $(`#cart-item-${id}`).fadeOut("slow");
                        }
                        // Refreshes the totals box. Works for both removing items and updating quantity.
                        $("#totals-box").fadeTo("slow", 0, function () {
                            $(`#totals-box`).html("").load(cartRefresh);
                            $(`#totals-box`).delay(400).fadeTo("slow", 1);
                        });
                    }
                // Send the message if anything else occurs.
                } else {
                    toastMessage(data.content.tag, data.content.message);
                }
            },
        });
    }
    $(`.toggle-form`).on("submit", function (ev) {
        // stops form from sending
        ev.preventDefault();

        // The ID of the product clicked.
        var id = this.id.slice(3);

        // The data sent in the form POST request.
        var serializedData = $(this).serialize();

        // The URL that the POST data would be sent to.
        var formUrl = this.action;

        // Fires the main ajax function
        like(id, serializedData, formUrl);
    });
}
