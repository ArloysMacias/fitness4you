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
        """Hadle payment intent succeeded webhook from Stripe """
        return HttpResponse(
            content=f'Webhook received: {event["typer"]}',
            status=200
        )

    def handle_payment_failed(self, event):
        """Hadle payment intent failed webhook from Stripe """
        return HttpResponse(
            content=f'Webhook received: {event["typer"]}',
            status=200
        )
