$(document).ready(function(){
    $("#id_country").change(function(){
        var selectedCountry = $(this).children("option:selected").val();
        if (selectedCountry == "") {
            $('.select-dropdown').css('color', '#aab7c4');
        }
        else if (selectedCountry !=""){
            $('.select-dropdown').css('color', 'black');
        }
    });
});