from rest_framework import serializers
from boards.models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
        #fields = ('id', 'song', 'singer', 'last_modify_date', 'created')