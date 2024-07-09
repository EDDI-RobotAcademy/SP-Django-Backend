from rest_framework import viewsets, status
from rest_framework.response import Response
from kakaoOauth.service.redis_service_impl import RedisServiceImpl
from travel_orders.service.travel_orders_service_impl import TravelOrderServiceImpl
class TravelOrdersView(viewsets.ViewSet):
    travelOrderService = TravelOrderServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def createOrders(self, request):
        try:
            data = request.data
            print('ordered data :', data)

            # 로그인 시 redis에 의해 변환된 userToken을 통해 accoundId에 접근
            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            if not accountId:
                raise ValueError('Invalid User Token')

            orderItemList = data.get('items')
            print(f"orderItemList : {orderItemList}")

            # 고객 id와 고객이 산 물품들을 가지고 주문 번호를 만든다.
            orderId = self.travelOrderService.createOrder(accountId, orderItemList)
            return Response(orderId, status=status.HTTP_200_OK) # 돈이 쓰이는 과정이라 유저 정보 항상 확인

        except Exception as e:
            print('주문 과정 중 에러 발생')
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def readOrders(self, request, orderId):
        try:
            data = request.data
            print(f'data: {data}, orderId: {orderId}')

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)
            print(f"accountId: {accountId}")

            if not accountId:
                raise ValueError('Invalid userToken')

            order = self.travelOrderService.readOrderDetails(orderId, accountId)
            print(f"controller return order : {order}")
            return Response(order, status=status.HTTP_200_OK)

        except Exception as e:
            print('주문 상세 내역 조회 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def orderList(self, request):
        data = request.data
        print(f"data : {data}")
        userToken = data.get('userToken')

        if not userToken:
            return Response({'error': 'User token is required'}, status=status.HTTP_400_BAD_REQUEST)

        # redis를 통해 account Id 할당
        accountId = self.redisService.getValueByKey(userToken)
        if not accountId:
            return Response({'error': 'Invalid user token'}, status=status.HTTP_400_BAD_REQUEST)
        print(f"accountId : {accountId}")
        # cartList를 찾는 방법 : 현재 cart에는 cart와 cartitem table로 구성
        # 먼저 누구의 카트인지를 찾고, 거기에 있는 장바구니들을 반환하면 됨
        travelOrders = self.travelOrderService.travelOrderList(accountId)

        # value(orderId)만 뽑아서 list화 시키기
        travelOrdersList = list(travelOrders.values())
        return Response(travelOrdersList , status=status.HTTP_200_OK)