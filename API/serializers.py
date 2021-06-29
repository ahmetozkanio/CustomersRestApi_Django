from rest_framework import serializers
from .models import Customer



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        # fields = ('alis','satis') // belirtilen kisimlari ceker.
        # fields = '__all__' // tum kisimlari ceker.
        fields = '__all__'