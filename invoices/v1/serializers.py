from rest_framework import serializers
from invoices.models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for InvoiceDetail model.
    Handles serialization and validation for individual invoice details.
    """
    class Meta:
        model = InvoiceDetail
        fields = ['id', 'description', 'quantity', 'price', 'line_total']


class InvoiceSerializer(serializers.ModelSerializer):
    """
    Serializer for Invoice model, including nested InvoiceDetail serializer.
    Allows creation and update of invoices along with their details in a single request.
    """
    details = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['id', 'invoice_number', 'customer_name', 'date', 'details']

    def create(self, validated_data):
        """
        Create an invoice and its associated details.
        param:
            validated_data (dict): Validated data for creating an invoice.
        return:
            Invoice: The created invoice instance.
        """
         
        details_data = validated_data.pop('details')
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return invoice

    def update(self, instance, validated_data):
        """
        Update an existing invoice and replace its details with the provided data.
        param:
            instance (Invoice): The invoice instance to be updated.
            validated_data (dict): Validated data for updating the invoice.
        return:
            Invoice: The updated invoice instance.
        """
        details_data = validated_data.pop('details')
        
        instance.invoice_number = validated_data.get('invoice_number', instance.invoice_number)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.date = validated_data.get('date', instance.date)
        instance.save()

        instance.details.all().delete()
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=instance, **detail_data)
        return instance
