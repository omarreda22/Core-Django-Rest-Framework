import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def api_first(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)  # take string of json data -> python dict
    except:
        pass
    print(data)
    # return JsonResponse({"omar": "reda"})
    return JsonResponse(data)
