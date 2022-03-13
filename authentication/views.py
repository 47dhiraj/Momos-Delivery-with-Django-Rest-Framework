from .models import User
from rest_framework import generics, status
from . import serializers
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

# Note : GenericAPIView ko get(), post(), put(), patch(), delete() jasta inbuilt method haru huncha 

class UserSerializer(generics.GenericAPIView):
    serializer_class = serializers.UserCreationSerializer

    @swagger_auto_schema(operation_summary = "Register/Create a new user by signing up.")
    def post(self, request):
        data = request.data                                         # post request ma aayeko data lai access gareko
        serializer = self.serializer_class(data = request.data)     # data lai UserCreationSerializer ma pass gareko & it returns serialized data

        if serializer.is_valid():                                   # serializers.py ko validate() method lai call garcha
            serializer.save()                                       # serializers.py ko create() method lai call garcha

            return Response(data = serializer.data, status = status.HTTP_201_CREATED)

        return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)


