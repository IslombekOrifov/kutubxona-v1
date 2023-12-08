from django.shortcuts import render, get_object_or_404

from rest_framework.generics import GenericAPIView

from rest_framework import (
    response, status, serializers
)

from .models import Faq, Contract, ContractUser, Certificate
from .serializers import (
    FaqSerializer, ContractSerializer, ContractUserSerializer,
    CertificateSerializer
    # CertificateSerializer,
)


class FaqListAPIView(GenericAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
    

class ContractCreateAPIView(GenericAPIView):
    queryset = Contract.objects.filter(is_active=True)
    serializer_class = ContractSerializer
    
    def post(self, request, *args, **kwargs):
        mutable_data = request.POST.copy()
        mutable_data_files = request.FILES.copy()
        u_count = mutable_data.get('u_count')
        users = []
        for i in range(int(u_count)):
            user_data = {}
            user_data['full_name'] = mutable_data.get(f'full_name_{i}', '')
            user_data['position'] = mutable_data.get(f'position_{i}', '')
            user_data['phone'] = mutable_data.get(f'phone_{i}', '')
            user_data['passport_data'] = mutable_data.get(f'passport_data_{i}', '')
            user_data['jshshir'] = mutable_data.get(f'jshshir_{i}', '')
            user_data['passport_file'] = mutable_data_files.get(f'passport_file_{i}', '')
            users.append(user_data)

        files = request.FILES
        if not users:
            raise serializers.ValidationError("The 'users' list is empty.")

        mutable_data.pop('users', None)  # Remove 'users' from the mutable copy
        contract_serializer = ContractSerializer(data=mutable_data)
        contract_serializer.is_valid(raise_exception=True)
        users_serializer = ContractUserSerializer(data=users, many=True)
        users_serializer.is_valid(raise_exception=True)
        contract_instance = contract_serializer.save()
        users_serializer.save(contract=contract_instance)

        return response.Response(status=status.HTTP_201_CREATED)


class CertificateGetAPIView(GenericAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    
    def post(self, request, *args, **kwargs):
        cert_data = self.get_serializer(data=request.data)
        cert_data.is_valid(raise_exception=True)
        datas = cert_data.validated_data
        datas.pop('full_name')
        certificate = Certificate.objects.filter(**datas).get()
        if certificate:
            status1 = status.HTTP_200_OK
            certificate_data = self.get_serializer(certificate).data
        else:
            certificate_data = None
            status1 = status.HTTP_204_NO_CONTENT
        return response.Response(certificate_data, status=status1)