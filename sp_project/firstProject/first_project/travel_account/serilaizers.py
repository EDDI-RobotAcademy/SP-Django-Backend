from rest_framework import serializers

from travel_account.entity.travel_account import TravelAccount


class TravelAccountSerializer(serializers.ModelSerializer):
    loginType = serializers.CharField(source='loginType.loginType', read_only=True)
    roleType = serializers.CharField(source='roleType.roleType', read_only=True)

    class Meta:
        model = TravelAccount
        fields = ['id', 'loginType', 'roleType']