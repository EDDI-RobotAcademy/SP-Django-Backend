import random

from django.db import transaction

from survey.entity.models import Survey
from travel_account.entity.travel_account import TravelAccount
from travel_orders.entity.travel_orders_item import TravelOrdersItem
from travel.entity.models import Travel
from travel_account.entity.profile import Profile
from travel_orders.entity.travel_orders import TravelOrders
from travel_orders.entity.travel_orders_status import TravelOrdersStatus

travels = list(Travel.objects.all())
account_ids = list(TravelAccount.objects.values_list('id', flat=True)) # 어떤식으로 나오는지 찍어보기 values_list가 뭔지?

def create_account(login_type_id, role_type_id, nickname, email):
    unique_nickname = nickname
    count = 1
    # 이미 있는 닉네임이라면, 닉네임 뒤에 count 추가
    while Profile.objects.filter(nickname=unique_nickname).exists():
        unique_nickname = f"{nickname}_{count}"
        count += 1
    # 랜덤 계정 생성 (같은 accountID에 대한 account, profile)
    account = TravelAccount.objects.create(loginType_id=login_type_id, roleType_id=role_type_id)
    Profile.objects.create(id=account.id, nickname=unique_nickname, email=email, account_id=account.id)
    return account.id

def create_random_order(account_id):
    try:
        with transaction.atomic():
            order = TravelOrders.objects.create(account_id=account_id, status=TravelOrdersStatus.PENDING)

            travel = random.choice(travels) # 여행지 중 random 선택 (객체임)
            price = travel.travelPrice # travel entity의 travelPrice 접근

            TravelOrdersItem.objects.create(
                orders=order,
                travel=travel,
                price=price,
            )
    except Exception as e:
        print(f"Error creating order for account {account_id}: {e}")

def create_random_survey(account_id):
    try:
        with transaction.atomic():
            Survey.objects.create(
                id=account_id,
                age=random.randint(10,100),
                gender=random.randint(1,2),
                travelConcept=random.randint(1,6),
                travelCompanion=random.randint(1,5),
                snsFrequency=random.randint(1,4),
                photoFrequency=random.randint(1,4),
                travelBudget=random.randint(1,5)
            )
    except Exception as e:
        print(f"Error creating order for account {account_id}: {e}")

if len(account_ids) < 12 :
    print(f"account_ids : {account_ids}")
    for i in range(len(account_ids), 12):
        nickname = f"User{i + 1}"
        email = f"user{i+1}@example.com"
        account_id = create_account(1,1,nickname,email)
        account_ids.append(account_id)

        # 각 계정 생성하자마자 설문조사 진행 할 것이므로 여기서 설문조사 함수 실행
        create_random_survey(account_id)

for _ in range(100):
    account_id = random.choice(account_ids) # 랜덤으로 account_ids 중 하나의 계정을 뽑음
    create_random_order(account_id)  # 선택한 계정에 대해 주문을 작성

print("sample data generation completed")
