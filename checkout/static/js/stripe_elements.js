var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = {
    base: {
        color: "#32325d",
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
            color: "#aab7c4"
        }
    },
    invalid: {
        color: "#fa755a",
        iconColor: "#fa755a"
    }
};

var card = elements.create('card', {style: style});

card.mount('#stripe-card-input');

let displayError = document.getElementById('card-errors');

//Validation errors on the card div
card.addEventListener('change', function (event) {
    if (event.error) {
        let html = `<i class="material-icons">error</i>${event.error.message}</span>`;
        $(displayError).html(html);
    } else {
        displayError.textContent = '';
    }
});

//On submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({'disable': true});
    $('#submit-button').attr('disable', true)
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: 'Jenny Rosen'
            }
        }
    }).then(function (result) {
        if (result.error) {
            let html = `<i class="material-icons">error</i>${result.error.message}</span>`;
            $(displayError).html(html);
            console.log(result.error.message);
            card.update({'disable': false});
            $('#submit-button').attr('disable', false)
        } else {
            // The payment has been processed!
            if (result.paymentIntent.status === 'succeeded') {
                form.submit()
                // Show a success message to your customer
                // There's a risk of the customer closing the window before callback
                // execution. Set up a webhook or plugin to listen for the
                // payment_intent.succeeded event that handles any business critical
                // post-payment actions.
            }
        }
    });
});

