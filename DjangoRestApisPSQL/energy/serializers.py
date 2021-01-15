from django.db.models import fields
from rest_framework import serializers
from .models import Wdmodel


class WdmodelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Wdmodel
		fields = (
			'id',
			'title',
			'description',
			'published'
		)