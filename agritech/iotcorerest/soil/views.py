from django.shortcuts import render

# Create your views here.


def soil_screen_view(request):
    #print(request.headers)
    context = {}
    context['some_string']="this is some string"
    return render(request, 'soil/soil.html', context)
