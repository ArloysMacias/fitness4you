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
        print("It call the webhook")
    except ValueError as e:
        # Invalid payload
        print("Invalid payload")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print("Invalid signature")
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        print("Bad request")
        return HttpResponse(content=e, status=400)

    handler = StripeWH_Handler(request)

    event_map = {
        'payment_succeeded': handler.handle_payment_intent_succeeded,
        'payment_failed': handler.handle_payment_intent_payment_failed,

    }

    event_type = event['type']
    event_handler = event_map.get(event_type, handler.handle_event)

    response = event_handler(event)

    return response
