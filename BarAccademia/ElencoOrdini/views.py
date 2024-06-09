from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import Ordine
from dotenv import load_dotenv
import os

load_dotenv()
bearer_token = os.getenv("BEARER_TOKEN")

@method_decorator(csrf_exempt, name='dispatch')
class AddObjectView(View):
    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            data = json.loads(request.body)
            if data.get("bearer_token")==bearer_token:
                date=data.get('data')
                client=data.get('cliente')
                product=data.get('prodotto')
                receipt_number=data.get('n_scontrino')
                obj = Ordine(data=date, cliente=client, prodotto=product, n_scontrino=receipt_number)
                obj.save()
                return JsonResponse({'status': 'success', 'id': obj.id})
            else:
                return HttpResponseForbidden("403 Forbidden")
        else:
            return JsonResponse({'status': 'error bad method'})
    

