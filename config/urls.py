from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def frontend(request):
    return render(request, 'index.html')

def devtools_json(request):
    return JsonResponse({})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
    path('.well-known/appspecific/com.chrome.devtools.json', devtools_json),
    path('', frontend),
]

