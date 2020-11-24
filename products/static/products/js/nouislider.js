function setGetParameter() {
    var lower = document.getElementById('skip-value-lower').value;
    var upper = document.getElementById('skip-value-upper').value;
    window.location.href = "{% url 'products' %}" + "?skip-value-lower=" + lower + "&skip-value-upper=" + upper;
};

$(document).ready(function () {
    var slider = document.getElementById('test-slider');
    noUiSlider.create(slider, {
        start: [document.getElementById('skip-value-lower').value, document.getElementById('skip-value-upper').value],
        connect: true,
        step: 1,
        orientation: 'horizontal', // 'horizontal' or 'vertical'
        range: {
            'min': 0,
            'max': 400
        },
        // pips: {
        //     format: wNumb({
        //         decimals: 2,
        //         prefix: '$'
        //     })
        // }
    });
    var skipValues = [
        document.getElementById('skip-value-lower'),
        document.getElementById('skip-value-upper')
    ];

    slider.noUiSlider.on('update', function (values, handle) {
        skipValues[handle].value = values[handle];
    })
});
