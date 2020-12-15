$(document).ready(function(){
    $("#id_country_default").change(function(){
        var selectedCountry = $(this).children("option:selected").val();
        if (selectedCountry == "") {
            $('.select-dropdown').css('color', '#d1d1d1');
        }
        else if (selectedCountry !=""){
            $('.select-dropdown').css('color', 'black');
        }
    });
});