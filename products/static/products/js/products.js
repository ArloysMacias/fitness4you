$(document).ready(function () {
    $('#myTable').pageMe({
        pagerSelector: '#myPager',
        activeColor: 'red',
        perPage: 16,
        showPrevNext: true,
        nextText: 'Prev',
        prevText: 'Next',
        hidePageNumbers: false
    });

    $("#wizard-picture").change(function () {
        readURL(this);
        var file = $('#wizard-picture')[0].files[0];
        $('#filename').text(`New Image:  ${file.name}`);
    });

    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#wizardPicturePreview').attr('src', e.target.result).fadeIn('slow');
            }
            reader.readAsDataURL(input.files[0]);
        }
    }

    var selectedCategory = $("#id_category").children("option:selected").val();

    if (selectedCategory == "0") {
        $('.select-dropdown').css('color', 'rgb(158 158 158)');
    } else {
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