
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from process.Updater import Updater


class ViewUpdaterEnabledPlacesProcess(View):
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        try:
            Updater.run()
            return HttpResponse("El método de actualizacion se ejecutó con éxito")
        except Exception as e:
                print(f"Error en la vista ViewUpdaterEnabledPlacesProcess: {str(e)}")
                return HttpResponse("Error en la vista ViewUpdaterEnabledPlacesProcess", status=500)