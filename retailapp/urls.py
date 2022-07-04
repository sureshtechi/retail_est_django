from django.urls import path
from . import views

urlpatterns = [
	path('create/', views.PostView.as_view(), name="create"),
	# path('list/', views.RetailList, name="retail_list"),
]