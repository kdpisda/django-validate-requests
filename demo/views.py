from django.shortcuts import render
from rest_framework import status
from django.http import JsonResponse
from demo import validators
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

# Create your views here.
@csrf_exempt
@require_http_methods(["POST"])
def simple_api(request):
    res = {}
    status_code = status.HTTP_200_OK
    try:
        req = json.loads(request.body.decode("utf-8"))
    except Exception as e:
        res["details"] = "Invalid request body"
    validation = validators.validate_api(req)
    if not validation["success"]:
        res["errors"] = validation["errors"]
        status_code = status.HTTP_400_BAD_REQUEST
    else:
        res["details"] = "Validation passed"
    return JsonResponse(res, status=status_code)