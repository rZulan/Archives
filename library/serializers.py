from rest_framework import serializers

from . import models

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Document
        fields = ['title', 'abstract']
    
    def create(self, data):
        return models.Document.objects.create(**data)
    
    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.abstract = data.get('abstract', instance.abstract)

        instance.save()
        return instance