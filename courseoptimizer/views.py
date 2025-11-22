from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Create your views here.


def index(request):
    return HttpResponse("hello world")


@csrf_exempt
@require_http_methods(["POST"])
def get_suggested_courses(request):
    try:
        # Parse JSON body
        body = json.loads(request.body)

        # Example processing: echo back with metadata
        response_data = {
            "received_array": body,
            "length": len(body),
            "status": "success",
        }

        suggested_courses = [
            "CIS 4930",
            "CDA 4205",
            "CDA 4205L",
            "CDA 4321",
            "CIS 4930",
        ]

        mock_data = {"suggested_courses": suggested_courses, "status": "success"}

        return JsonResponse(mock_data)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON in request body"}, status=400)
    except Exception as e:
        return JsonResponse(
            {"error": "An unexpected error occurred", "detail": str(e)}, status=500
        )
