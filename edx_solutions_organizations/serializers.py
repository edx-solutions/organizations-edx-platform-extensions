""" Django REST Framework Serializers """

from rest_framework import serializers

from .models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    """ Serializer for Organization model interactions """
    url = serializers.HyperlinkedIdentityField(view_name='organization-detail')

    class Meta:
        """ Serializer/field specification """
        model = Organization
        fields = ('url', 'id', 'name', 'display_name', 'contact_name', 'contact_email', 'contact_phone',
                  'logo_url', 'users', 'groups', 'created', 'modified', 'salesforce_id', 'additional_metadata',
                  'migrated_to_docebo', 'docebo_redirect_url', 'docebo_sso_enabled',)
        read_only = ('url', 'id', 'created')
        extra_kwargs = {'users': {'allow_empty': True}, 'groups': {'allow_empty': True}}


class BasicOrganizationSerializer(serializers.ModelSerializer):
    """ Serializer for Basic Organization fields """
    url = serializers.HyperlinkedIdentityField(view_name='organization-detail')

    class Meta:
        """ Serializer/field specification """
        model = Organization
        fields = ('url', 'id', 'name', 'display_name', 'contact_name', 'contact_email', 'contact_phone',
                  'logo_url', 'created', 'modified', 'salesforce_id', 'additional_metadata', 'migrated_to_docebo',
                  'docebo_redirect_url', 'docebo_sso_enabled',)
        read_only = ('url', 'id', 'created',)


class OrganizationWithCourseCountSerializer(BasicOrganizationSerializer):
    """ Serializer for Organization fields with number of courses """
    number_of_courses = serializers.IntegerField()
    number_of_participants = serializers.IntegerField()

    class Meta:
        """ Serializer/field specification """
        model = Organization
        fields = ('url', 'id', 'name', 'display_name', 'number_of_courses', 'contact_name', 'contact_email',
                  'contact_phone', 'logo_url', 'created', 'modified', 'number_of_participants', 'salesforce_id',
                  'additional_metadata', 'migrated_to_docebo', 'docebo_redirect_url', 'docebo_sso_enabled',)


class OrganizationWithParticipantCountSerializer(BasicOrganizationSerializer):
    """ Serializer for Organization fields with number of participants """
    number_of_participants = serializers.IntegerField()

    class Meta:
        """ Serializer/field specification """
        model = Organization
        fields = ('url', 'id', 'name', 'display_name', 'contact_name', 'contact_email',
                  'contact_phone', 'logo_url', 'created', 'modified', 'number_of_participants', 'salesforce_id',
                  'additional_metadata', 'migrated_to_docebo', 'docebo_redirect_url', 'docebo_sso_enabled',)


class OrganizationAttributesSerializer(serializers.ModelSerializer):
    """ Serializer for Organization Attributes interactions """

    class Meta:
        """ Serializer/field specification """
        model = Organization
        fields = ('attributes', 'id')

    def to_representation(self, instance):
        return instance.get_all_attributes()
