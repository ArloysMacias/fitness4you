$(document).ready(function(){
    var selectedCountry = $("#id_country").children("option:selected").val();
    if (selectedCountry === "") {
        $('.select-dropdown').css('color', '#aab7c4');
        $('#country-world').css('display', 'flex');
    }
    else{
        $('.select-dropdown').css('color', 'black');
        $('#country-world').css('display', 'none');
    }

    $("#id_country").change(function(){
        var selectedCountry = $(this).children("option:selected").val();
        if (selectedCountry === "") {
            $('.select-dropdown').css('color', '#aab7c4');
            $('#country-world').css('display', 'flex');
        }
        else{
            $('#country-world').css('display', 'none');
            $('.select-dropdown').css('color', 'black');
        }
    });

    $("#id-save-info").on('change', function() {
        if (this.checked) {
            $(this).attr("checked", 'checked');
        }else {
            $(this).attr("checked",false);
        }
    });

});