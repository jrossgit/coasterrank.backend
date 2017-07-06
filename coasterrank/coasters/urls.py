from django.conf.urls import url

import views

urlpatterns = [
    url(r'^rollercoasters/', views.RollerCoasterListView.as_view(), name='rollercoaster-list'),
]