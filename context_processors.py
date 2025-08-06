import os

def google_api_key(request):
    return {
        "API_KEY": os.getenv("GOOGLE_MAPS_API_KEY")
    }
