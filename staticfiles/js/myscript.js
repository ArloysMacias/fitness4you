$(document).ready(function(){

    initializeMaterialize()

});

function initializeMaterialize() {
    $('.collapsible').collapsible();
    $('select').material_select();
    document.querySelectorAll('.select-wrapper').forEach(t => t.addEventListener('click', e=>e.stopPropagation())) // fixes first click
    $(".button-collapse").sideNav();
    $('.dropdown-buttonh').dropdown();
    $('.parallax').parallax();
    $('.modal').modal();
    // $('.materialboxed').materialbox();
}