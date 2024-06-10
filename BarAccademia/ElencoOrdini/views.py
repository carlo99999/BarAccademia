from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import Ordine
from dotenv import load_dotenv
import os
import datetime
from datetime import datetime
import pytz

load_dotenv()
bearer_token = os.getenv("BEARER_TOKEN")

@method_decorator(csrf_exempt, name='dispatch')
class AddObjectView(View):
    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            rome_tz = pytz.timezone('Europe/Rome')

            data = json.loads(request.body)
            if data.get("bearer_token")==bearer_token:
                if data.get("date")==None:
                    date= datetime.now(rome_tz)
                else:
                    if not isinstance(data.get("date"), datetime):
                        date= datetime.now(rome_tz)
                client=data.get('cliente')
                if client == None:
                    return JsonResponse({'status': 'error', 'message': 'cliente is required'})
                product=data.get('prodotto')
                if product == None:
                    return JsonResponse({'status': 'error', 'message': 'prodotto is required'})
                receipt_number=data.get('n_scontrino')
                if receipt_number == None:
                    return JsonResponse({'status': 'error', 'message': 'n_scontrino is required'})
                if date!=None:
                    obj = Ordine(data=date, cliente=client, prodotto=product, n_scontrino=receipt_number)
                obj.save()
                return JsonResponse({'status': 'success', 'id': obj.id})
            else:
                return HttpResponseForbidden("403 Forbidden")
        else:
            return JsonResponse({'status': 'error bad method'})
    

