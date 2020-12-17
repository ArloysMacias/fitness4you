$(document).ready(function () {
    var selectedCategory = $("#id_category").children("option:selected").val();
    if (selectedCategory == "0") {
        $('.select-dropdown').css('color', 'rgb(158 158 158)');
    }
    else{
        $('.select-dropdown').css('color', 'black');
    }

    $("#id_category").change(function () {
        var selectedCategory = $(this).children("option:selected").val();
        if (selectedCategory == "0") {
            $('.select-dropdown').css('color', 'rgb(158 158 158)');
        } else {
            $('.select-dropdown').css('color', 'black');
        }
    });
});