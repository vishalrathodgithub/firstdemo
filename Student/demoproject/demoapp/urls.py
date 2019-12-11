from django.urls import path
from demoapp.views import Display,json_view
urlpatterns=[
path('app/',Display),
path('app1/',json_view),

]
