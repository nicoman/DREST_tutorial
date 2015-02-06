# -*- coding: utf-8 -*-
from django.forms import widgets
from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # The sourceargument controls which attribute is used to populate a field
    # and can point any attribute on the serialized instance
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Because 'snippets' is a reverse relationship on the User model, it will
    # not be included by default when using the ModelSerializer class, so we
    # needed to add an explicit field for it.
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')