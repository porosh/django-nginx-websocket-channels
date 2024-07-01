from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path

def test_websocket_view(request):
    file_path = Path(__file__).resolve().parent.parent / 'static' / 'test_websocket.html'
    content = file_path.read_text()
    return HttpResponse(content)

# Create your views here.
