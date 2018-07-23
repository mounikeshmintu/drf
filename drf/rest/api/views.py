from rest_framework.views import APIView
from .serializers import statusSerializer
from rest.models import status
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from rest_framework.response import Response
from rest_framework import mixins
import json
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions

from django.shortcuts import get_object_or_404

# class StatusListSearchApi(APIView):
#     def get(self,request,format=None):
#         qs=status.objects.all()
#         serializer=statusSerializer(qs,many=True)
#         return Response(serializer.datax)
    # ListAPIView

class StatusListSearchApi(mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
     ListAPIView
    ):
    permissions_classes=[permissions.IsAuthenticated]
    authentication_classes=[SessionAuthentication]




    queryset=status.objects.all()
    serializer_class=statusSerializer
    lookup_field='id'
    def get_queryset(self):
        request = self.request
        print(request.user)
        qs = status.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs
    def get_object(self):
        request=self.request
        passed_id=request.GET.get('id',None)
        queryset=self.get_queryset()
        obj=None
        if passed_id is not None:
            obj=get_object_or_404(queryset,id=passed_id)
            self.check_object_permissions(request,obj)
        return obj
    def get(self,request,*args,**kwargs):
        passed_id=request.GET.get('id',None)
        # json_data=json.loads(request.body)
        # new_passed_id=json_data.get('id',None)
        if passed_id is not None:
            return self.retrieve(request,*args,**kwargs)
        return super().get(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    #
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

# class StatusDetailApiView(RetrieveAPIView):
#     queryset=status.objects.all()
#     serializer_class=statusSerializer
#     lookup_field='id'
# class StatusUpdateApiView(UpdateAPIView):
#     queryset=status.objects.all()
#     serializer_class=statusSerializer
#     lookup_field='id'
# class StatusDeleteApiView(DestroyAPIView):
#     queryset=status.objects.all()
#     serializer_class=statusSerializer
#     lookup_field='id'
