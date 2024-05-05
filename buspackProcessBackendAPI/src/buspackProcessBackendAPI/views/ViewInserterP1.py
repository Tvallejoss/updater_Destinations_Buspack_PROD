from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from process.inserter.InserterP1 import InserterP1
from django.http import JsonResponse

class ViewInserterP1(View):
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        try:
            data = InserterP1.run()  # Suponiendo que InserterP1.run() devuelve una lista de objetos
            serialized_data = []
            for obj in data:
                serialized_data.append({
                    'idog': obj.idlocality,
                    'zip_code': obj.zip_code,
                    'province_name': obj.province_name,
                    'locality_name': obj.locality_name,
                    'enabled_place': obj.enabled_place,
                    'isActive': obj.isActive,
                    'code' : obj.code
                })
            return JsonResponse(serialized_data, safe=False)
        except Exception as e:
            # Manejar errores aquí
            return JsonResponse({'error': str(e)}, status=500)