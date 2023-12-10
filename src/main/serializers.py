from rest_framework import serializers

from .models import (
    Slider, News, Result, LeaderAndTrener, Partner,
    UserContact, Region, CenterContact, CenterSocial, 
    CenterInfo, CenterStructure, DocumentCategory, 
    Document, Branch, Event, EventImages
)


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        exclude = ["is_active", 'created']
        

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ["is_active", 'is_news', 'created']


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class TrenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderAndTrener
        exclude = ["is_leader", 'work_time', 'phone', 'email']
        

class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderAndTrener
        exclude = ["is_leader", 'telegram', 'instagram', 'facebook']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Update the image URL to include the full path
        representation['image'] = self.context['request'].build_absolute_uri(instance.image.url)
        return representation
        

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        exclude = ['name', 'is_active']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Update the image URL to include the full path
        representation['logo'] = self.context['request'].build_absolute_uri(instance.logo.url)
        return representation
        

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContact
        fields = '__all__'
        extra_kwargs = {
            'created': {'read_only': True, 'required': False},
        }

class CenterSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterSocial
        fields = '__all__'


class CenterContactSerializer(serializers.ModelSerializer):
    socials = CenterSocialSerializer(many=True)
    class Meta:
        model = CenterContact
        fields = "__all__"


class CenterInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterInfo
        exclude = ['is_history',]
        
    
class CenterStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterStructure
        fields = "__all__"



class DocumentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentCategory
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        exclude = ['category',]
        
        
class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        exclude = ['region',]


class EventImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImages
        fields = ('image',)


class EventSerializer(serializers.ModelSerializer):
    images = EventImagesSerializer(many=True)
    class Meta:
        model = Event
        fields = ('id', 'name_uz', 'name_ru', 'name_en',
                  'description_uz', 'description_ru', 'description_en',
                  'about_uz', 'about_ru', 'about_en',
                  'image', 'images', 'created')


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ['is_active',]