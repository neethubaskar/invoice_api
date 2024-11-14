# Invoice API

This is a simple Django REST Framework API for managing invoices and their details. The API allows you to create and update invoices along with multiple invoice details through a single request using nested serializers.

## Features

- **Create Invoice**: Add a new invoice with multiple details (items).
- **Update Invoice**: Update an existing invoice and replace the old details with new ones provided in the request.

## Requirements

- Python 3.8+
- Django 3.2+
- Django REST Framework

## Getting Started

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/neethubaskar/invoice_api.git
cd invoice_api
```

### Step 2: Build and Run the Docker Containers

docker-compose up --build

### Step 3: Run Migrations

docker-compose exec web python manage.py migrate

### Step 4: Create a Superuser

docker-compose exec web python manage.py createsuperuser

## API Endpoints

### Create an Invoice

- Endpoint: invoice/api/v1/create_invoices/
- Method: POST
- Description: Creates a new invoice with multiple line items (details).

```bash

{
  "invoice_number": "INV001",
  "customer_name": "John Doe",
  "date": "2024-11-12",
  "details": [
    {
      "description": "Product A",
      "quantity": 2,
      "price": 50.00,
      "line_total": 100.00
    },
    {
      "description": "Product B",
      "quantity": 1,
      "price": 75.00,
      "line_total": 75.00
    }
  ]
}
```

### Update an Invoice

- Endpoint: invoice/api/v1/update_invoices/<id>/
- Method: PUT
- Description: Updates an existing invoice by its primary key, replacing its line items (details) with the new data provided.

```bash
{
  "invoice_number": "INV001",
  "customer_name": "John Doe",
  "date": "2024-11-12",
  "details": [
    {
      "description": "Product A Updated",
      "quantity": 3,
      "price": 60.00,
      "line_total": 180.00
    }
  ]
}

