$(document).ready(function(){
    $('.collapsible').collapsible();
    $('select').material_select();
    document.querySelectorAll('.select-wrapper').forEach(t => t.addEventListener('click', e=>e.stopPropagation())) // fixes first click
    $(".button-collapse").sideNav();
    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        close: 'Ok',
        closeOnSelect: false, // Close upon selecting a date,
        defaultTime: 'now'
    });
    $('.datepicker').on('mousedown',function(event){ event.preventDefault(); })
    $('.carousel').carousel({
        duration:120,
        dist:-150,
        numVisible:6
    });
    $('.modal').modal();
    $('.parallax').parallax();
});