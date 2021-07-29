from django.urls import path 
from .views import PhoneDetailsView, PhoneListView

urlpatterns = [
   
    path('', PhoneListView.as_view(), name ='phones_api'),
    path('<int:pk>/', PhoneDetailsView.as_view(), name ='phone_details')
]