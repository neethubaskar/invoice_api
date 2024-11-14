from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('invoices.v1.urls'))
]