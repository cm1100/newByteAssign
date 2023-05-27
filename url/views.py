import datetime

from django.shortcuts import render
from rest_framework import viewsets,permissions
from url.models import UrlDetail
from url.serializers import UrlDetailSerializer
from rest_framework.decorators import action
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.



class UrlDetailViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.AllowAny]
    serializer_class = UrlDetailSerializer
    queryset = UrlDetail.objects.all()
    http_method_names = ['get','post']

    def create(self, request, *args, **kwargs):
        if request.data.get('url',None):
            hashed_url=hash(request.data['url']+str(datetime.datetime.now()))
            if hashed_url<0:
                hashed_url*=-1
            request.data['hashed_url']=hashed_url
        response = super(UrlDetailViewSet, self).create(request,*args,**kwargs)
        return response



    @action(methods=['GET'], detail=False,url_path='get_by_hash/(?P<hashed_url>\d+)')
    def get_by_hash(self,request,hashed_url):
        url_detail=UrlDetail.objects.filter(hashed_url =hashed_url).first()

        if not url_detail:
            return JsonResponse({'message':'Hash not found'},status=404)

        if url_detail.use_limit!=None and url_detail.used_count>=url_detail.use_limit :
            return JsonResponse({'message':'Url has expired'},status=404)

        url_detail.used_count+=1
        url_detail.save()

        return JsonResponse(model_to_dict(url_detail))