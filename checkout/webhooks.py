from django.views.decorators.csrf import csrf_exempt

from fitness4you import settings
from django.http import HttpResponse
from checkout.webhook_handler import StripeWH_Handler
from django.views.decorators.http import require_POST
import stripe


# Using Django
@require_POST
@csrf_exempt
def webhook(request):
    # Stripe setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify the signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # # Handle the event
    # if event.type == 'payment_intent.succeeded':
    #     payment_intent = event.data.object  # contains a stripe.PaymentIntent
    #     print('PaymentIntent was successful!')
    # elif event.type == 'payment_method.attached':
    #     payment_method = event.data.object  # contains a stripe.PaymentMethod
    #     print('PaymentMethod was attached to a Customer!')
    # # ... handle other event types
    # else:
    #     print('Unhandled event type {}'.format(event.type))

    handler = StripeWH_Handler(request)

    event_map = {
        'payment_succeeded': handler.handle_payment_succeeded,
        'payment_failed': handler.handle_payment_failed,

    }

    event_type = event['type']
    event_handler = event_map.get(event_type, handler.handle_event)

    response = event_handler(event)

    print('AAAAAAA')

    return response
