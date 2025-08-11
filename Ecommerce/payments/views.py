from django.shortcuts import redirect
from django.http import JsonResponse
from .paypal import create_order, capture_order

def start_payment(request):
    order = create_order(amount="10.00")  # $10
    for link in order["links"]:
        if link["rel"] == "approve":
            return redirect(link["href"])
    return JsonResponse({"error": "No approval URL found"})

def payment_success(request):
    order_id = request.GET.get("token")
    result = capture_order(order_id)
    return JsonResponse(result)

def payment_cancel(request):
    return JsonResponse({"status": "Payment cancelled"})
