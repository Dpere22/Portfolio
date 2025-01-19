import { $ } from "/static/jquery/src/jquery.js";

$('.project').css('cursor', 'pointer').on("click", function () {
    window.location.href = $(this).data("href")
})
