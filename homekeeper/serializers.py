from rest_framework import serializers
from homekeeper.models import Homekeeper

class HomekeeperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Homekeeper
        fields = (
            'hk_id',
            'create_date',
            'pay_date',
            'inout',
            'contents',
            'money',
        )

