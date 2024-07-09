from django.shortcuts import render
from ipware import get_client_ip
import requests, json


def index(request):
    client_ip = get_client_ip(request)
    response = requests.get(f"http://ip-api.com/json/{client_ip}")
    l_data = response.text
    ldata = json.loads(l_data)
    return render(request, "index.html", context={"data": ldata})
