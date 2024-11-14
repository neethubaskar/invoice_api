from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from invoices.models import Invoice
from .serializers import InvoiceSerializer

class InvoiceView(APIView):
    
    def post(self, request):
        """
        Handle POST requests to create a new invoice along with its details.
        param:
            request (Request): The HTTP request containing invoice data in JSON format.
        return:
            Response: HTTP response with the created invoice data or validation errors.
        """
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Handle PUT requests to update an existing invoice and its details.
        param:
            request (Request): The HTTP request containing updated invoice data in JSON format.
            pk (int): Primary key of the invoice to be updated.
        return:
            Response: HTTP response with the updated invoice data or errors if not found/invalid.
        """
        try:
            invoice = Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            return Response({'error': 'Invoice not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
