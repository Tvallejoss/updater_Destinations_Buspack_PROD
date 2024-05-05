

from django.http import HttpResponse
from django.views import View
import json
from django.http import JsonResponse

class ViewLogin(View):
    def post(self, request, *args, **kwargs):
        try:
            ## Es un login protocolar, Debido a eso la simplicidad.
            data = json.loads(request.body.decode('utf-8'))
            user_value = data.get("user")
            user_password = data.get("password")
            if user_value == "adminBuspack@1" and user_password == "PaSSword@1":
                print(5)
                return JsonResponse("Acceso Otorgado", safe = False)
            else:
                return JsonResponse({'error': "Acceso Denegado"}, status=404, safe = False)
            
        except Exception as e:
                print(f"Acceso Denegado: {str(e)}")
                return JsonResponse({'error': str(e)}, status=404)

            