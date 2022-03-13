from django.shortcuts import get_object_or_404
from .models import Order
from rest_framework import generics, status
from . import serializers
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from drf_yasg.utils import swagger_auto_schema

from authentication.models import User

# Alternative way of importing User:
# from django.contrib.auth import get_user_model
# User = get_user_model()

# Another Alternative way:
# from .models import User



# Create your views here.

class OrderView(generics.GenericAPIView):
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary = "Get all Orders")
    def get(self, request):
        orders = Order.objects.all().filter(customer = request.user)
        serializer = self.serializer_class(instance=orders, many=True)  # Dherai objects or queryset fetch garera lyauna cha vani many=True lekhincha

        return Response(data = serializer.data, status = status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary = "Place/Create an order") 
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data = data)

        if serializer.is_valid():                                       # serializer ma validate() vanni inbuilt method huncha, tesailai call gareko
            serializer.save(customer = request.user)                    # serializer ma create() method huncha, tesailai call gareko

            # print(f"\n {serializer.data}")

            return Response(data = serializer.data, status=status.HTTP_201_CREATED)

        return Response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)   



class OrderIdView(generics.GenericAPIView):
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary = "View the detail of an order by its ID")
    def get(self, request, order_id):
        order = get_object_or_404(Order, pk = order_id)         # by default id lai pk lekhincha
        
        if order.customer == request.user: 
            serializer = self.serializer_class(instance = order)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        
        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN) 


    @swagger_auto_schema(operation_summary = "Update an order by its ID")
    def put(self,request,order_id):
        order = get_object_or_404(Order, pk=order_id)

        if order.customer == request.user: 
            serializer = self.serializer_class(instance = order, data=request.data)

            if serializer.is_valid():
                serializer.save()

                return Response(data=serializer.data,status=status.HTTP_200_OK)

            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)

    @swagger_auto_schema(operation_summary = "Delete an order by its ID")
    def delete(self, request,order_id):

        order = get_object_or_404(Order,id=order_id)

        if order.customer == request.user: 
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)



class UpdateOrderStatusView(generics.GenericAPIView):
    serializer_class = serializers.OrderStatusUpdateSerializer
    permission_classes=[IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(operation_summary = "Admin/Superuser can update the status of an order.")
    def put(self, request, order_id):
        order = get_object_or_404(Order, pk = order_id)
        serializer = self.serializer_class(instance = order, data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(status = status.HTTP_200_OK, data = serializer.data)

        return Response(status = status.HTTP_400_BAD_REQUEST, data = serializer.errors)



class UserOrdersView(generics.GenericAPIView):
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(operation_summary="Admin can view all orders made by a specific user")
    def get(self, request, user_id):
        user = User.objects.get(pk = user_id)
        orders = Order.objects.all().filter(customer = user)

        serializer = self.serializer_class(instance=orders, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)



class UserOrderDetailView(generics.GenericAPIView):
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(operation_summary = "Admin can view detail of an order made by a specific user")
    def get(self, request, user_id, order_id):
        user = User.objects.get(pk = user_id)
        order = Order.objects.get(customer=user, pk=order_id)
        # Alternative Code : order = get_object_or_404(Order, customer = user, pk = order_id)
        
        serializer = self.serializer_class(instance = order)

        return Response(data = serializer.data, status = status.HTTP_200_OK)

