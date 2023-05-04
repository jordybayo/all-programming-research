import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Update
from django.views.generic import View
from cfeapi.mixins import JsonResponseMixin
from django.core.serializers import serialize
# Create your views here.

# def detial_view(request):
#     return render() # return JSON data -> js Objects Notion
#     return HttpResponse(get_template().render({}))


def json_example_view(request):
    '''
    URI -- for a rest API
    '''
    data = {
        "count":1000,
        "content" : "some data here"
    }
    return JsonResponse(data)


class JsonCBV(View):
    def get(self, request, *args, **kargs):
        data = {
            "count" : 1000,
            "content" : "Some new content"
        }
        return JsonResponse(data)



class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count":1000,
            "content" : "some data here"
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *arg, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data, content_type="application/json")