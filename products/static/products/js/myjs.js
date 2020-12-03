$(document).ready(function () {

    $('#handleCounter').handleCounter({
        minimum: 1,
        maximize: null,

        onChange: function(){
            document.getElementById('quantity').value+=document.getElementById('quantity').value;
        },
        onMinimum: function(){
            document.getElementById('quantity').value-=document.getElementById('quantity').value;
        },
        // onMaximize: function(){}
    });
});