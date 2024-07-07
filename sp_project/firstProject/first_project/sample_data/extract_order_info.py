import os
import django
import pandas as pd
from travel_orders.entity.travel_orders_item import TravelOrdersItem
from travel.entity.models import Travel
from travel_account.entity.travel_account import TravelAccount

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")
django.setup()

def export_orders_to_excel(file_path):
    # order와 travel이 엮인 TravelOrdersItem 내용 반환
    orders_items = TravelOrdersItem.objects.select_related('orders', 'travel').all()

    # print(f"orders_items : {orders_items}")
    # <TravelOrdersItem: TravelOrderItem 17 for TravelOrder 20>, <TravelOrdersItem: TravelOrderItem 18 for TravelOrder 21>
    # TravelOrderItem과 TravelOrder에 둘 다 접근 가능해짐

    data = []
    for order_item in orders_items:
        order = order_item.orders
        travel = order_item.travel
        data.append({
            'accountId': order.account_id,
            'travelId': travel.travelId,
            'price': order_item.price
        })

    df = pd.DataFrame(data)

    df.to_excel(file_path, index=False, engine='openpyxl')
    print(f"Exported orders data to {file_path}")


file_path = "travel_orders_data.xlsx"
export_orders_to_excel(file_path)