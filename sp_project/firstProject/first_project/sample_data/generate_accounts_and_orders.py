import random
from datetime import datetime, timedelta

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
# 랜덤 날짜를 위함
start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 6, 31)
last_date = start_date
# 랜덤 날짜 생성기
def random_date(start, end):
    delta = end - start
    int_delta = delta.days * 24 * 60 * 60 + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

# DB에 오름차순 날짜로 저장하는 함수
def create_ordered_dates(account_id):
    try:
        # 해당 account_id의 최근 주문 내역 가져오기
        latest_record = TravelOrders.objects.filter(account_id=account_id).order_by('-created_date').first()
        # 주문 내역 중 create_date 정보만 가져오기
        print(f"latest_record : {latest_record.created_date}")
        latest_record = latest_record.created_date
        # offset error 방지를 위해 timezone 없애기
        latest_record = latest_record.replace(tzinfo=None)

    # 해당 account id에 가져올게 없다면(주문을 한 번도 안 한 상태) start date로 넣기
    except:
        latest_record = start_date
    new_date = random_date(latest_record, end_date)
    # last_date = new_date
    # print(f"new_date : {new_date}")
    return new_date

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
            random_created_at = create_ordered_dates(account_id)
            # print(random_created_at)
            order = TravelOrders.objects.create(
                account_id=account_id, status=TravelOrdersStatus.PENDING, created_date=random_created_at)

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

if len(account_ids) < 35 :
    print(f"account_ids : {account_ids}")
    for i in range(len(account_ids), 35):
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
