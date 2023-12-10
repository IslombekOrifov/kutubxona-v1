from django.db import models

from main.models import Region

from ckeditor.fields import RichTextField

from .services import upload_course_path


class Course(models.Model):
    name = models.CharField(max_length=250)
    sub_name = models.CharField(max_length=250)
    duration = models.CharField(max_length=50)
    description = RichTextField()
    image = models.ImageField(upload_to=upload_course_path)
    amount = models.PositiveIntegerField()
    is_online = models.BooleanField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self) -> str:
        return self.name

    
class CourseApplication(models.Model):
    course = models.ForeignKey(Course,
                               on_delete=models.PROTECT,
                               related_name='applications')
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=16)
    region = models.ForeignKey(Region,
                               on_delete=models.PROTECT,
                               related_name='applications')
    work_place = models.CharField(max_length=150)
    is_checked = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self) -> str:
        return self.full_name
