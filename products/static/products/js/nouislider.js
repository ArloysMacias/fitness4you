$(document).ready(function () {
    var slider = document.getElementById('test-slider');
    noUiSlider.create(slider, {
        start: [document.getElementById('skip-value-lower').value, document.getElementById('skip-value-upper').value],
        connect: true,
        step: 2,
        orientation: 'horizontal',
        tooltips: [wNumb({
            prefix: '€',
            decimals: 1
        }), wNumb({
            prefix: '€',
            decimals: 1
        })],
        range: {
            'min': 0,
            'max': 400
        },
        pips: {
            mode: 'range',
            density: 2,
            format: wNumb({
                prefix: '€',
                decimals: 1
            })
        },
        // format: wNumb({
        //     decimals: 3,
        //     thousand: '.',
        //     suffix: ' (US $)'
        // })
    });
    var rangeValues = [
        document.getElementById('skip-value-lower'),
        document.getElementById('skip-value-upper')
    ];

    slider.noUiSlider.on('update', function (values, handle) {
        rangeValues[handle].value = values[handle];
    })

    var inputFormat_lower = document.getElementById('skip-value-lower');
    var inputFormat_upper = document.getElementById('skip-value-lower');
    inputFormat_lower.addEventListener('change', function () {
        slider.noUiSlider.set(this.value);
    });
    inputFormat_upper.addEventListener('change', function () {
        slider.noUiSlider.set(this.value);
    });

});
