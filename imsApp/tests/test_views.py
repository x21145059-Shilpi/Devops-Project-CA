from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from mixer.backend.django import mixer
import pytest
from imsApp.views import *

@pytest.mark.django_db
class TestViews:
    
    def test_home(self):
        #mixer.blend('products.Product')
        path = reverse('home-page')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = home(request)
        assert response.status_code == 200
        
    def test_login(self):
        #mixer.blend('products.Product')
        path = reverse('login')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = home(request)
        assert response.status_code == 200
        
    def test_logout(self):
        #mixer.blend('products.Product')
        path = reverse('logout')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = home(request)
        assert response.status_code == 200
        
    def test_UpdateProfile(self):
        #mixer.blend('products.Product')
        path = reverse('update-profile')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = home(request)
        assert response.status_code == 200
        
    def test_UpdatePasswords(self):
        #mixer.blend('products.Product')
        path = reverse('update-password')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = home(request)
        assert response.status_code == 200
        
    def test_Profile(self):
        #mixer.blend('products.Product')
        path = reverse('profile')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = home(request)
        assert response.status_code == 200
        
    def test_Category(self):
        #mixer.blend('products.Product')
        path = reverse('category-page')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = home(request)
        assert response.status_code == 200
        
    def test_SaveCategory(self):
        #mixer.blend('products.Product')
        path = reverse('save-category')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = home(request)
        assert response.status_code == 200
        
    def test_ManageCategory(self):
        #mixer.blend('products.Product')
        path = reverse('manage-category')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = home(request)
        assert response.status_code == 200

        