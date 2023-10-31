from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from library import models
from library import serializers

class Documents(APIView):
    def get(self, request):
        documents = models.Document.objects.all()

        if(documents):
            serializer = serializers.DocumentSerializer(documents, many=True)

            return Response(serializer.data, status=status.HTTP_302_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request):
        serializer = serializers.DocumentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        
class Document(APIView):
    def get(self, request, pk):
        try:
            document = models.Document.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.DocumentSerializer(document)
        return Response(serializer.data)
    
    def put(self, request, pk):
        document = models.Document.objects.get(id=pk)
        serializer = serializers.DocumentSerializer(document, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def delete(self, request, pk):
        document = models.Document.objects.get(id=pk)
        document.delete()
        return Response({"deleted": True}, status=status.HTTP_200_OK)
