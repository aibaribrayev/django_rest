from decimal import Decimal 
from django.test import TestCase
from core import models 


class ModelTests(TestCase): 
    """Test models."""
    def test_create_company(self): 
        company = models.Company.objects.create(
            name = "Sample company name",
        )
        self.assertEqual(str(company), company.name)
    
    def test_create_item(self): 
        item = models.Item.objects.create(
            name = 'Item1'
        )
        self.assertEqual(str(item), item.name)
    