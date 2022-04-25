'''from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestModels:

    def test_Category(self):
        category = mixer.blend('imsApp.Category', name='xyz', description='category', status="Active")
        assert category.name == 'xyz'
        assert category.description == 'category'
        assert category.status == 'Active'
        
    def test_Product(self):
        product = mixer.blend('imsApp.Product', code='xyz', name='abc', description='product', price=120, status='Active')
        assert product.code== 'xyz'
        assert product.name == 'abc'
        assert product.description == 'product'
        assert product.price == 120
        assert product.status == 'Active'
        
    def test_Stock(self):
        stock = mixer.blend('imsApp.Stock', quantity=20, type='Stock-in', status='Active')
        assert stock.quantity == 20
        assert stock.type == 'Stock-in'
        assert stock.status == 'Active'
        
    def test_Invoice(self):
        invoice = mixer.blend('imsApp.Invoice', transaction='abc', customer='xyz', total=30)
        assert invoice.transaction == 'abc'
        assert invoice.customer=='xyz'
        assert invoice.total == 30
        
    def test_Invoice_Item(self):
        item = mixer.blend('imsApp.Invoice_Item', price=20, quantity=30)
        assert item.price == 20
        assert item.quantity == 30'''
    