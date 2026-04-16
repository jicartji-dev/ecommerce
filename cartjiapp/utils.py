from django.utils.timezone import now
from .models import Order

def generate_order_id():
    year = now().year

    # 🔥 get last order based on order_id (NOT id)
    last_order = Order.objects.filter(
        order_id__startswith=f"CJ-{year}"
    ).order_by("-order_id").first()

    if last_order:
        last_number = int(last_order.order_id.split("-")[-1])
        new_number = last_number + 1
    else:
        new_number = 1

    return f"CJ-{year}-{str(new_number).zfill(4)}"