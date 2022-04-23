from django.urls import reverse, resolve
class TestUrls:
    
    def test_admin_url(self):
        path = reverse('redirect-admin')
        assert resolve(path).view_name == 'redirect-admin'
   
    def test_login_url(self):
        path = reverse('login')
        assert resolve(path).view_name == 'login'
        
    def test_user_url(self):
        path = reverse('login-user')
        assert resolve(path).view_name == 'login-user'
        
    def test_register_url(self):
        path = reverse('register-user')
        assert resolve(path).view_name == 'register-user'
        
    def test_logout_url(self):
        path = reverse('logout')
        assert resolve(path).view_name == 'logout'
        
    def test_profile_url(self):
        path = reverse('profile')
        assert resolve(path).view_name == 'profile'
        
    def test_update_url(self):
        path = reverse('update-profile')
        assert resolve(path).view_name == 'update-profile'
        
    def test_password_url(self):
        path = reverse('update-password')
        assert resolve(path).view_name == 'update-password'
        
    def test_home_url(self):
        path = reverse('home-page')
        assert resolve(path).view_name == 'home-page'
        
    def test_category_url(self):
        path = reverse('category-page')
        assert resolve(path).view_name == 'category-page'
        
    def test_manage_url(self):
        path = reverse('manage-category')
        assert resolve(path).view_name == 'manage-category'
        
    def test_save_url(self):
        path = reverse('save-category')
        assert resolve(path).view_name == 'save-category'
        
    def test_delete_url(self):
        path = reverse('delete-category')
        assert resolve(path).view_name == 'delete-category'
        
    def test_product_url(self):
        path = reverse('product-page')
        assert resolve(path).view_name == 'product-page'
        
    def test_manage_product_url(self):
        path = reverse('manage-product')
        assert resolve(path).view_name == 'manage-product'
        
    def test_delete_product_url(self):
        path = reverse('delete-product')
        assert resolve(path).view_name == 'delete-product'
        
    def test_inventory_page_url(self):
        path = reverse('inventory-page')
        assert resolve(path).view_name == 'inventory-page'
        
    def test_save_stock_url(self):
        path = reverse('save-stock')
        assert resolve(path).view_name == 'save-stock'
        
    def test_delete_stock_url(self):
        path = reverse('delete-stock')
        assert resolve(path).view_name == 'delete-stock'
        
    def test_sales_page_url(self):
        path = reverse('sales-page')
        assert resolve(path).view_name == 'sales-page'
        
    def test_get_product_url(self):
        path = reverse('get-product')
        assert resolve(path).view_name == 'get-product'
        
    def test_save_sales_url(self):
        path = reverse('save-sales')
        assert resolve(path).view_name == 'save-sales'
        
    def test_invoice_page_url(self):
        path = reverse('invoice-page')
        assert resolve(path).view_name == 'invoice-page'
        
    def test_delete_invoice_url(self):
        path = reverse('delete-invoice')
        assert resolve(path).view_name == 'delete-invoice'
