    var infinite = new Waypoint.Infinite({
        element: $(".infinite-container")[0],
        onBeforePageLoad: function () {
            $(".spinner-border").show();
        },
        onAfterPageLoad: function () {
            $(`.toggle-form`).off("submit");
            $(".spinner-border").hide();
            buttonToggle(liked, unliked, carted, uncarted, likeUpdate, cartUpdate);
        },
    });