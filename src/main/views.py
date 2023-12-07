from django.shortcuts import render

from rest_framework.generics import (
    GenericAPIView, ListAPIView, 
    CreateAPIView, RetrieveAPIView
    
)

from rest_framework import (
    response,
    status
)

from .models import (
    Slider, News, Result, LeaderAndTrener, Partner,
    CenterContact, CenterInfo, CenterStructure, 
    DocumentCategory, Document, Branch, Event, EventImages,
    Region, UserContact
)

from .serializers import (
    SliderSerializer, NewsSerializer, ResultSerializer,
    TrenerSerializer, PartnerSerializer, CenterContactSerializer,
    CenterInfoSerializer, LeaderSerializer, CenterStructureSerializer,
    DocumentCategorySerializer, DocumentSerializer, BranchSerializer,
    EventImagesSerializer, EventSerializer, EventListSerializer,
    RegionSerializer, UserContactSerializer
)

from competition.models import CompetetionQuestion
from competition.serializers import CompetetionQuestionSerializer


class MainAPIView(GenericAPIView):
    queryset = Slider.objects.filter(is_active=True).order_by('-created')
    serializer_class = SliderSerializer
    
    def get(self, request, *args, **kwargs):
        sliders = Slider.objects.filter(is_active=True).order_by('-created')
        sliders_serializer = SliderSerializer(sliders, many=True)
        
        news = News.objects.filter(is_active=True, is_news=True).order_by('-created')[:12]
        news_serializer = NewsSerializer(news, many=True)
        
        elon = News.objects.filter(is_active=True, is_news=False).order_by('-created')[:3]
        elon_serializer = NewsSerializer(elon, many=True)
        
        results = Result.objects.last()
        results_serializer = ResultSerializer(results)
        
        treners = LeaderAndTrener.objects.filter(is_leader=False)[:12]
        treners_serializer = TrenerSerializer(treners, many=True)
        
        partner = Partner.objects.filter(is_active=True)[:12]
        partner_serializer = PartnerSerializer(partner, many=True)
        
        contacts = CenterContact.objects.all().prefetch_related('socials').last()
        contacts_serializer = CenterContactSerializer(contacts)
        
        education = CompetetionQuestion.objects.filter(education=True, is_active=True)
        education_serializer = CompetetionQuestionSerializer(education, many=True)
        
        regions = Region.objects.all()
        regions_serializer = RegionSerializer(regions, many=True)
        return response.Response({'sliders': sliders_serializer.data,
                                  'news': news_serializer.data,
                                  'elon': elon_serializer.data,
                                  'results': results_serializer.data,
                                  'treners': treners_serializer.data,
                                  'partner': partner_serializer.data,
                                  'contacts': contacts_serializer.data,
                                  'education': education_serializer.data,
                                  'regions': regions_serializer.data})
    

class CenterHistoryAPIView(GenericAPIView):
    queryset = CenterInfo.objects.filter(is_history=True)
    serializer_class = CenterInfoSerializer
    
    def get(self, request, *args, **kwargs):
        instance = self.get_queryset().last()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)


class CenterConfirmationAPIView(GenericAPIView):
    queryset = CenterInfo.objects.filter(is_history=False)
    serializer_class = CenterInfoSerializer
    
    def get(self, request, *args, **kwargs):
        instance = self.get_queryset().last()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)
    

class LeadersAPIView(GenericAPIView):
    queryset = LeaderAndTrener.objects.filter(is_leader=True)
    serializer_class = LeaderSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


class CenterStructureAPIView(GenericAPIView):
    queryset = CenterStructure.objects.all()
    serializer_class = CenterStructureSerializer
    
    def get(self, request, *args, **kwargs):
        instance = CenterStructure.objects.last()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)


class DocumentCategoryAPIView(GenericAPIView):
    queryset = DocumentCategory.objects.all()
    serializer_class = DocumentCategorySerializer
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
    

class DocumentAPIView(GenericAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(category=kwargs['pk'])
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
    

class BranchAPIView(GenericAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    
    def get(self, request, *args, **kwargs):
        instance = self.get_queryset().filter(region=kwargs['pk']).last()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)


class EventListAPIView(GenericAPIView):
    queryset = Event.objects.filter(is_active=True)
    serializer_class = EventListSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
    

class EventDetailAPIView(GenericAPIView):
    queryset = Event.objects.filter(is_active=True)
    serializer_class = EventSerializer
    
    def get(self, request, *args, **kwargs):
        instance = self.get_queryset().filter(id=kwargs['pk']).prefetch_related('images').last()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)
    
    
class UserContactCreateAPIView(GenericAPIView):
    queryset = UserContact.objects.all()
    serializer_class = UserContactSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(status=status.HTTP_201_CREATED)