import os
import django
import pandas as pd
from travel_orders.entity.travel_orders_item import TravelOrdersItem
from survey.entity.models import Survey
from travel.entity.models import Travel
from travel_account.entity.travel_account import TravelAccount

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")
django.setup()

def export_survey_to_excel(file_path):
    # order와 travel이 엮인 TravelOrdersItem 내용 반환
    # TravelOrderItem과 TravelOrder 둘 다 접근 하기 위함
    survey_items = Survey.objects.all()

    data = []
    for survey_item in survey_items:
        # order = survey_item.orders
        data.append({
            'accountId': survey_item.id,
            'age': survey_item.age,
            'gender': survey_item.gender,
            'travelConcept': survey_item.travelConcept,
            'travelCompanion': survey_item.travelCompanion,
            'snsFrequency': survey_item.snsFrequency,
            'photoFrequency': survey_item.photoFrequency,
            'travelBudget': survey_item.travelBudget,
        })

    df = pd.DataFrame(data)

    df.to_excel(file_path, index=False, engine='openpyxl')
    print(f"Exported orders data to {file_path}")


file_path = "survey_data.xlsx"
export_survey_to_excel(file_path)