from .models import Shops
from .serializers import ShopSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics


class ShopList(APIView):
    def get(self, request, format = None):
        shops = Shops.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# class ShopList(generics.ListCreateAPIView):
#     queryset = Shops.objects.all()
#     serializer_class = ShopSerializer

# class ShopDetail(generics.ListCreateAPIView):
#     queryset = Shops.objects.get_queryset()
#     serializer_class = ShopSerializer



class ShopDetail(APIView):
    def get_object(self, pk):
        try:
            return Shops.objects.get(pk=pk)
        except Shops.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        shops = self.get_object(pk)
        serializer = ShopSerializer(shops)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        shops = self.get_object(pk)
        serializer = ShopSerializer(shops, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        shops = self.get_object(pk)
        shops.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


