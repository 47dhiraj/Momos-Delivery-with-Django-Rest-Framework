from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    order_status = serializers.HiddenField(default = "PENDING")                 # serializer ko HiddeenField ma frontend batw value halna pani mildaina, just default tarikale databsae ma save hune kaam matra ho
    size = serializers.CharField(max_length = 25)
    plate_quantity = serializers.IntegerField()
    flavour = serializers.CharField(max_length = 40)
    placed_at = serializers.DateTimeField(read_only=True)


    class Meta:
        model = Order 
        fields = ['order_status', 'size', 'plate_quantity','flavour', 'placed_at']             # jun jun field lai serializable garaune ho tyo tyo field lai yaha mention garni



class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(max_length=25)
    # updated_at = serializers.DateTimeField()

    class Meta:
        model = Order
        fields = ['order_status']


