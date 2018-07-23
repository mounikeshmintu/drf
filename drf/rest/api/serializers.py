from rest.models import status
from rest_framework import serializers


class statusSerializer(serializers.ModelSerializer):
    class Meta:
        model=status
        fields=['id','user','content','image']
        read_only_fields=['user']
    def validate(self,value):
        if len(value)>10000:
            raise serializers.ValidationError("the input is way too big ")
        return value
    def validate_email(self,data):
        content=data.get('content')
        if content == "":
            content=None
        image=data.get('image')
        if content is None  and image is None :
            raise serializers.ValidationError('either image or content should be preset')
