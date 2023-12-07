import base64
import six
import uuid
import os

from django.core.files.base import ContentFile

from rest_framework import serializers

from .models import Faq, Contract, ContractUser
   
   
class Base64FileField(serializers.FileField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_file')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64FileField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        image_extension = imghdr.what(file_name, decoded_file)
        if image_extension:
            return "jpg" if image_extension == "jpeg" else image_extension


        _, file_extension = os.path.splitext(file_name)
        file_extension = file_extension.lower()[1:]

        supported_extensions = ['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx']

        if file_extension in supported_extensions:
            return file_extension
        else:
            self.fail('invalid_file', format=file_extension)

    def __init__(self, *args, **kwargs):
        kwargs['error_messages'] = {
            'invalid_file': 'Неверный формат файла. Поддерживаемые форматы: pdf, jpg, jpeg, png, doc, docx.',
        }
        super().__init__(*args, **kwargs)


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = "__all__"
              

class ContractUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractUser
        fields = ('full_name', 'position', 'phone', 
                  'passport_data', 'jshshir', 'passport_file')
        
        
class ContractSerializer(serializers.ModelSerializer):
    u_count = serializers.IntegerField()
    class Meta:
        model = Contract
        fields = ('contract_type', 'is_company', 'region', 
                  'organization', 'organization_director',
                  'payment_percent', 'phone', 'rek_org_name', 
                  'rek_org_address', 'rek_org_bank', 'rek_org_hisob_raqam', 
                  'rek_org_account_hisob_raqam', 'rek_org_mfo',
                  'rek_org_inn', 'rek_org_inn_gazna', 'u_count'
                  )
    
    def create(self, validated_data):
        extra_field_value = validated_data.pop('u_count', None)
        instance = super(ContractSerializer, self).create(validated_data)
        return instance

    def update(self, instance, validated_data):
        extra_field_value = validated_data.pop('u_count', None)
        instance = super(ContractSerializer, self).update(instance, validated_data)
        return instance


class ContractUserCertSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractUser
        fields = ('passport_data', 'jshshir')
         

# class CertificateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ContractUser
#         fields = ('certificate',)