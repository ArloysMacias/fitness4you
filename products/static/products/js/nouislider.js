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
        //         prefix: '$ ',
        //         decimals: 3
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
