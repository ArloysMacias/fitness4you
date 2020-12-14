from django.http import HttpResponse


class StripeWH_Handler:
    """"Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Hadle a generic /unknow/unexpected webhook event"""
        return HttpResponse(
            content=f'Webhook received: {event["typer"]}',
            status=200
        )

    def handle_payment_succeeded(self, event):
        """Hadle payment_intent_succeeded webhook from Stripe """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["typer"]}',
            status=200
        )

    def handle_payment_failed(self, event):
        """Hadle payment_intent_failed webhook from Stripe """
        return HttpResponse(
            content=f'Webhook received: {event["typer"]}',
            status=200
        )
