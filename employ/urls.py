from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("user_create/", UserCreateView.as_view(), name="user_create"),
    path("work_list/", WorkListView.as_view(), name="work_list"),
    path("work_create/", WorkCreateView.as_view(), name="work_create"),
    path("work_detail/<int:pk>/", WorkDetailView.as_view(), name="work_detail"),
    path("application_create/<int:pk>/", ApplicationCreateView.as_view(), name="application_create"),
    path("application_list/", ApplicationListView.as_view(), name="application_list"),
    path("application_detail/<int:pk>/", ApplicationDetailView.as_view(), name="application_detail"),
    path("application_update/<int:pk>/", ApplicationUpdateView.as_view(), name="application_update"),
    path("application_delete/<int:pk>/", ApplicationDeleteView.as_view(), name="application_delete"),
    path("work_update/<int:pk>/", WorkUpdateView.as_view(), name="work_update"),
    path("work_delete/<int:pk>/", WorkDeleteView.as_view(), name="work_delete"),
]
