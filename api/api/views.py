from django.http import JsonResponse
from .models import api
from .serializers import ApiSerializer

def api_list(request):
    apis = api.objects.all()
    serializer = ApiSerializer(apis, many=True)
    return JsonResponse({ "response_code": 0, 'results': serializer.data}, safe=False)