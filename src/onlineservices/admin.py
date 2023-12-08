from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from import_export.admin import ImportMixin

from .models import Faq, Contract, ContractUser, Certificate


@admin.register(Faq)
class FaqAdmin(TranslationAdmin):
    list_display = ('question',)


class ContractUserAdmin(admin.TabularInline):
    model = ContractUser
    raw_id_fields = ['contract']


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'region', 'is_company', 'organization', 
                    'contract_type', 'payment_percent', 'contract_file', 'is_active', 
                    'is_checked', 'is_confirmed', 'created')
    list_filter = ('is_checked', 'is_active', 'is_confirmed', 'created', 'is_company',)
    ordering = ('-created', 'is_checked', 'is_active', 'is_confirmed', )
    inlines = [ContractUserAdmin]
    

@admin.register(Certificate)
class CertificateAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('id', 'cert_number', 'cert_date', 'full_name', 'position', 
                    'created')
    list_filter = ('cert_number', 'created')
    ordering = ('-created',)
