console.log("activated");

$(".home-categories").bind("mouseenter mouseleave", function () {
    jQueryTest = jQuery(this).find("h3").text();
    targetElement = $(".product_detail:first-child:first-child:contains(" + jQueryTest + ")");
    targetElement.toggleClass("homehide", true);
    $(".product_detail:first-child:first-child").not(targetElement).toggleClass("homehide", false)
});

// $(".home-categories").bind("mouseout", function () {
//     jQueryTest = jQuery(this).find("h3").text();
//     targetElement = $(".product_detail:first-child:first-child:contains(" + jQueryTest + ")");
//     targetElement.toggleClass("homehide", false);
// });