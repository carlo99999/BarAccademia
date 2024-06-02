from django.urls import path
from .views import AddObjectView

urlpatterns = [
    path('new_scontrino/', AddObjectView.as_view(), name='add_object'),
]
