$(document).ready(function () {
    var slider = document.getElementById('test-slider');
    noUiSlider.create(slider, {
        start: [document.getElementById('lower').value, document.getElementById('upper').value],
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
        document.getElementById('lower'),
        document.getElementById('upper')
    ];

    slider.noUiSlider.on('update', function (values, handle) {
        rangeValues[handle].value = values[handle];
    })

    var inputFormat_lower = document.getElementById('lower');
    var inputFormat_upper = document.getElementById('upper');
    inputFormat_lower.addEventListener('change', function () {
        slider.noUiSlider.set(this.value);
    });
    inputFormat_upper.addEventListener('change', function () {
        slider.noUiSlider.set(this.value);
    });

});
