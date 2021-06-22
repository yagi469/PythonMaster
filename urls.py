from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  # main/urls.pyをインポート
  path('main/', include('main.urls')),
  path('admin/', admin.site.urls),
]
