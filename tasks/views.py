from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer


class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by("-created_at")
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# ✅ THIRD-PARTY API INTEGRATION
class ExchangeRateAPIView(APIView):
    def get(self, request):
        """
        Fetch live EUR -> USD exchange rate from a public third-party API
        """
        try:
            url = "https://api.exchangerate.host/latest?base=EUR&symbols=USD"
            response = requests.get(url, timeout=5)
            data = response.json()

            rate = data.get("rates", {}).get("USD")

            return Response({
                "source": "exchangerate.host",
                "base": "EUR",
                "target": "USD",
                "rate": rate
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": "Failed to fetch exchange rate"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

from django.shortcuts import render
from django.db.models import Count


# ✅ DASHBOARD REPORT
def dashboard_view(request):
    """
    Show task counts by status using a bar chart
    """
    task_counts = Task.objects.values("status").annotate(count=Count("id"))

    data = {
        "todo": 0,
        "in_progress": 0,
        "done": 0
    }

    for row in task_counts:
        data[row["status"]] = row["count"]

    context = {
        "todo": data["todo"],
        "in_progress": data["in_progress"],
        "done": data["done"],
    }

    return render(request, "tasks/dashboard.html", context)
