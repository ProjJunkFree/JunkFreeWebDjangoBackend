from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer
from rest_framework import status

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['category'] 
    search_fields = ['name', 'description']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        instance = serializer.save()  

class UserItemList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Item.objects.filter(user=request.user)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            item = Item.objects.get(id=pk, user=request.user)
        except Item.DoesNotExist:
            return Response({"error": "Item not found or does not belong to the user"}, status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

