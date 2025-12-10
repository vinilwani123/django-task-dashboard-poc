from django.urls import path
from .views import (
    TaskListCreateAPIView,
    TaskRetrieveUpdateDestroyAPIView,
    ExchangeRateAPIView,
    dashboard_view,
)

urlpatterns = [
    # ✅ DASHBOARD (ROOT PAGE)
    path("", dashboard_view, name="dashboard"),

    # ✅ CRUD APIs
    path("api/tasks/", TaskListCreateAPIView.as_view(), name="task-list-create"),
    path("api/tasks/<int:pk>/", TaskRetrieveUpdateDestroyAPIView.as_view(), name="task-detail"),

    # ✅ Third-party API
    path("api/exchange-rate/", ExchangeRateAPIView.as_view(), name="exchange-rate"),
]
