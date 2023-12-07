from django.db import models

from ckeditor.fields import RichTextField

from competition.models import CompetetionQuestion

from .services import (
    upload_slider_path, upload_news_path, upload_center_info_path, 
    upload_partner_path, upload_leader_trener_path, upload_branch_path, 
    upload_center_structure_path, upload_gallery_path,
    upload_document_path
)

class Slider(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=upload_slider_path)
    url = models.URLField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title

        
class News(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_news_path, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_news = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Result(models.Model):
    online = models.PositiveIntegerField()
    offline = models.PositiveIntegerField()

    def __str__(self):
        return f"online: {self.id}, offline: {self.offline}"
    
    def save(self, *args, **kwargs):
        if Result.objects.exists() and not self.pk:
            pass
        else:   
            return super(Result, self).save(*args, **kwargs)
        

class LeaderAndTrener(models.Model):
    full_name = models.CharField(max_length=50)
    about = models.CharField(max_length=70)
    image = models.ImageField(upload_to=upload_leader_trener_path)
    is_leader = models.BooleanField(default=True)
    work_time = models.CharField(max_length=15, blank=True)
    phone = models.CharField(max_length=16, blank=True)
    email = models.EmailField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.full_name
        
    
class Partner(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    logo = models.ImageField(upload_to=upload_partner_path)
    url = models.URLField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class UserContact(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=16, blank=True)
    academic_degree = models.ForeignKey(CompetetionQuestion,
                                        on_delete=models.SET_NULL,
                                        related_name='user_contacts',
                                        blank=True,
                                        null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.full_name} {self.phone}"
    
    
class Region(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
    
class CenterContact(models.Model):
    tel = models.CharField(max_length=16)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.tel

    def save(self, *args, **kwargs):
        if CenterContact.objects.exists() and not self.pk:
            pass
        else:   
            return super(CenterContact, self).save(*args, **kwargs)
        

class CenterSocial(models.Model):
    center = models.ForeignKey(CenterContact,
                               on_delete=models.PROTECT,
                               related_name='socials')
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=20)
    url = models.URLField()
    
    def __str__(self):
        return self.code
    
    def save(self, *args, **kwargs):
        if CenterSocial.objects.exists() and not self.pk:
            pass
        else:   
            return super(CenterSocial, self).save(*args, **kwargs)


class CenterInfo(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    body = models.TextField()
    file = models.FileField(upload_to=upload_center_info_path)
    is_history = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class CenterStructure(models.Model):
    image = models.ImageField(upload_to=upload_center_structure_path)
    
    def __str__(self):
        return f"{self.id}"
    
    def save(self, *args, **kwargs):
        if CenterStructure.objects.exists() and not self.pk:
            pass
        else:   
            return super(CenterStructure, self).save(*args, **kwargs)


class DocumentCategory(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=150)
    file = models.FileField(upload_to=upload_document_path)

    url = models.URLField()
    category = models.ForeignKey(DocumentCategory,
                                 on_delete=models.PROTECT,
                                 related_name='files')
    
    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=150)
    about = models.TextField()
    description = RichTextField()
    image = models.ImageField(upload_to=upload_branch_path)
    site = models.URLField()
    region = models.ForeignKey(Region,
                               on_delete=models.PROTECT,
                               related_name='branches')
    
    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    image = models.ImageField(upload_to=upload_gallery_path)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class EventImages(models.Model):
    event = models.ForeignKey(Event, 
                              on_delete=models.PROTECT,
                              related_name='images')
    image = models.ImageField(upload_to=upload_gallery_path)

    def __str__(self):
        return str(self.event.name)
    