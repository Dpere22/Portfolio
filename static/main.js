import { $ } from "/static/jquery/src/jquery.js";

$(".project").on("click", function () {
    window.location.href = $(this).data("href")
})