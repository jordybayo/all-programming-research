from rest_framework import generics
# from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

from status.models import Status
from .serializers import StatusSerializer

class StatusListSearchAPIView(APIView):
    permission_classes = []
    authentication_class = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)



class StatusAPIView(generics.ListAPIView):
    permission_classes          = []
    authentication_class        = []
    serializer_class            = StatusSerializer

    def get_queryset(self):
        # http://localhost:8000/api/status/?q=some
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs


class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes          = []
    authentication_class        = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class StatusDetailAPIView(generics.RetrieveAPIView):
    permission_classes          = []
    authentication_class        = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    lookup_field                = 'id'

    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id')
    #     return Status.objects.get(id=kw_id)