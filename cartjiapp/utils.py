import datetime
from .models import Order

def generate_order_id():
    year = datetime.date.today().year
    last_order = Order.objects.order_by("-id").first()
    if last_order:
        return f"CJ-{year}-{last_order.id + 1:04d}"
    return f"CJ-{year}-0001"
