$(document).ready(function(){
    var selectedCountry = $("#id_country_default").children("option:selected").val();
    if (selectedCountry == "") {
        $('.select-dropdown').css('color', '#aab7c4');
        $('#country-world').css('display', 'flex');
    }
    else{
        $('.select-dropdown').css('color', 'black');
        $('#country-world').css('display', 'none');
    }

    $("#id_country_default").change(function(){
        var selectedCountry = $(this).children("option:selected").val();
        if (selectedCountry == "") {
            $('.select-dropdown').css('color', '#aab7c4');
            $('#country-world').css('display', 'flex');
        }
        else{
            $('#country-world').css('display', 'none');
            $('.select-dropdown').css('color', 'black');
        }
    });
});