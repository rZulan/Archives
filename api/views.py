from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from library import models
from library import serializers

@api_view(['GET'])
def documents(request, *args, **kwargs):
    documents = models.Document.objects.all()
    serializer = serializers.DocumentSerializer(documents, many=True)

    return Response(serializer.data, status=status.HTTP_302_FOUND)

@api_view(['POST'])
def document_create(request, *args, **kwargs):
    serializer = serializers.DocumentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def document(request, pk):
    try:
        document = models.Document.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.DocumentSerializer(document)

        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = serializers.DocumentSerializer(document, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return serializer.errors
    
    if request.method == 'DELETE':
        document.delete()
        return Response(status=status.HTTP_200_OK)