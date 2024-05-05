from buspackProcessBackendAPI.views.ViewInserterP1 import ViewInserterP1
from buspackProcessBackendAPI.views.ViewInserterP2 import ViewInserterP2
from buspackProcessBackendAPI.views.ViewLogin import ViewLogin
from django.urls import path

from buspackProcessBackendAPI.views.ViewUpdaterEnabledPlacesProcess import ViewUpdaterEnabledPlacesProcess

urlpatterns = [
    path('runUpdaterEnabledPlacesProcess', ViewUpdaterEnabledPlacesProcess.as_view(), name='runUpdaterEnabledPlacesProcess'),
    path('runViewInserterP1', ViewInserterP1.as_view(), name='runViewInserterP1'),
    path('runViewInserterP2', ViewInserterP2.as_view(), name='runViewInserterP2'),
    path('login', ViewLogin.as_view(), name='login'),
]
