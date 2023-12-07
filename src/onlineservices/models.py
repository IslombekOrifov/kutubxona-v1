from django.db import models

from main.models import Region

from .services import upload_contract_user_path, upload_contract_file_path


class Faq(models.Model):
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=500)
    
    def __str__(self):
        return self.question
    
    
class Contract(models.Model):
    contract_number = models.CharField(max_length=30, blank=True, null=True)
    contract_file = models.FileField(upload_to=upload_contract_file_path, blank=True, null=True)
    
    contract_type = models.CharField(max_length=250, blank=True, null=True)
    is_company = models.BooleanField(default=False)
    region = models.ForeignKey(Region,
                               on_delete=models.PROTECT,
                               related_name='contracts')
    organization = models.CharField(max_length=150, blank=True)
    organization_director = models.CharField(max_length=150, blank=True)
    payment_percent = models.CharField(max_length=5)
    phone = models.CharField(max_length=16, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_checked = models.BooleanField(default=False, blank=True)
    is_confirmed = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    rek_org_name = models.CharField(max_length=250, blank=True, null=True)
    rek_org_address = models.CharField(max_length=250, blank=True, null=True)
    rek_org_bank = models.CharField(max_length=30, blank=True, null=True)
    rek_org_hisob_raqam = models.CharField(max_length=30, blank=True, null=True)
    rek_org_account_hisob_raqam = models.CharField(max_length=30, blank=True, null=True)
    rek_org_mfo = models.CharField(max_length=30, blank=True, null=True)
    rek_org_inn = models.CharField(max_length=30, blank=True, null=True)
    rek_org_inn_gazna = models.CharField(max_length=50, blank=True, null=True)
        
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return str(self.id)
        

class ContractUser(models.Model):
    full_name = models.CharField(max_length=150)
    contract = models.ForeignKey(Contract,
                               on_delete=models.PROTECT,
                               related_name='users')
    position = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=16)
    passport_data = models.CharField(max_length=10)
    jshshir = models.CharField(max_length=14)
    passport_file = models.FileField(upload_to=upload_contract_user_path, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_checked = models.BooleanField(blank=True, default=False)
    is_confirmed = models.BooleanField(blank=True, default=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self) -> str:
        return f"{self.full_name}"
    

class Certificate(models.Model):
    cert_number = models.CharField(max_length=10)
    cert_date = models.DateField(blank=True, null=True)
    full_name = models.CharField(max_length=150, blank=True, null=True)
    position = models.CharField(max_length=150, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.cert_number)