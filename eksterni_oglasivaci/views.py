from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import EksterniOglasivaci
from .serializers import EksterniOglasivaciSerializer

class EksterniOglasivaciAPIView(APIView):
    """
    API View to handle POST and PUT requests for EksterniOglasivaci.
    """

    def post(self, request, *args, **kwargs):
        """
        Handle POST request to create a new EksterniOglasivaci instance.
        """
        serializer = EksterniOglasivaciSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        """
        Handle PUT request to update an existing EksterniOglasivaci instance.
        """
        instance = get_object_or_404(EksterniOglasivaci, pk=pk)
        serializer = EksterniOglasivaciSerializer(instance, data=request.data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
