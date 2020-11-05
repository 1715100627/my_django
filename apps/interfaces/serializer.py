from rest_framework import serializers
from interfaces.models import Interfaces


class InterfacesModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        # filter=('id','name','leader','tester')
        # filter = '__all__'
        exclude = ('update_time', 'is_delete')
        # read_only_fields = ('leader', 'tester')
        extra_kwarge = {
            'create_time': {
                "read_only": True
            },
        }
