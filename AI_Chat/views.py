from django.shortcuts import render
from django.http import StreamingHttpResponse
from django_ratelimit.decorators import ratelimit
from .services import PerplexityService
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from openai import OpenAI
import json

# Create your views here.
def home(request):
    return render(request,"index.html")

def chat(request):
    return render(request,"chat.html")




async def stream_generator(user_message):
    full_response = []

    async for chunk in PerplexityService.stream_answer(user_message):
        full_response.append(chunk)
        yield chunk   

@csrf_exempt
async def chat_endpoint(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            message = body.get("message")

            if not message:
                return JsonResponse({"error":"No message provided"},status=400)
            
            response = StreamingHttpResponse(
            stream_generator(message),
            content_type="text/plain; charset=utf-8"
)
            response["Cache-Control"] = "no-cache"
            response["Connection"] = "keep-alive"
            response["X-Accel-Buffering"] = "no"   # IMPORTANT for proxies

            return response

        
        except json.JSONDecodeError:
            return JsonResponse({"error":"Invalid JSON"},status=400)
    return JsonResponse({"error":"MEthod not allowed"},status=405)