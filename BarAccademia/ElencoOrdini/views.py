from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import Ordine

@method_decorator(csrf_exempt, name='dispatch')
class AddObjectView(View):
    def post(self, request, *args, **kwargs):
        print(request.body)
        data = json.loads(request.body)
        
        date=data.get('data')
        client=data.get('cliente')
        product=data.get('prodotto')
        receipt_number=data.get('n_scontrino')
        obj = Ordine(data=date, cliente=client, prodotto=product, n_scontrino=receipt_number)
        obj.save()
        return JsonResponse({'status': 'success', 'id': obj.id})
    

