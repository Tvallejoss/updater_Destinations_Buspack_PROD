import json
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from process.inserter.InserterP2 import InserterP2
from django.http import JsonResponse

class ViewInserterP2(View):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            InserterP2.run(json_data)
            return JsonResponse("InserterP2 fue ejecutado correctamente", safe=False, status=200)
           
        except Exception as e:
                print(f"Error en la vista ViewInserterP2: {str(e)}")
                return JsonResponse({'Error en la vista ViewInserterP2': str(e)}, status=500)