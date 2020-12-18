$(document).ready(function () {

    $('#myTable').pageMe({
        pagerSelector: '#myPager',
        activeColor: 'red',
        perPage: 6,
        showPrevNext: true,
        nextText: 'Prev',
        prevText: 'Next',
        hidePageNumbers: false
    });

    var selectedCategory = $("#id_category").children("option:selected").val();

    if (selectedCategory == "0") {
        $('.select-dropdown').css('color', 'rgb(158 158 158)');
    }
    else{
        $('.select-dropdown').css('color', 'black');
    }

    $("#id_category").change(function () {
        var selectedCategory = $(this).children("option:selected").val();
        alert(selectedCategory)
        if (selectedCategory == "0") {
            $('.select-dropdown').css('color', 'rgb(158 158 158)');
        } else {
            $('.select-dropdown').css('color', 'black');
        }
    });

});