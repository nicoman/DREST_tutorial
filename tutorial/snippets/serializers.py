# -*- coding: utf-8 -*-
from django.forms import widgets
from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    # The sourceargument controls which attribute is used to populate a field
    # and can point any attribute on the serialized instance
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
    # Because 'snippets' is a reverse relationship on the User model, it will
    # not be included by default when using the ModelSerializer class, so we
    # needed to add an explicit field for it.
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')