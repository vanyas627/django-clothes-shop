from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import CategoriesProduct, Products

class ViewsTests(TestCase):
    def setUp(self):

        #Category
        self.category = CategoriesProduct.objects.create(
            title='Test Category',
            slug='Test-category',
            is_visible=True
        )

        #Product
        self.product = Products.objects.create(
            title='Test product',
            slug='Test-product',
            price=100,
            is_visible=True,
            is_featured=True
        )

        self.product.category.set([self.category])

        #User
        self.user = User.objects.create_user(username='testuser', password='12345678')

    def test_home_page(self):
        """Test home page"""

        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test product')

    def test_category_page(self):
        """Open page with products and check category"""
        url = reverse('category_products', args=[self.category.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Category")
        self.assertContains(response, "Test product")

    def test_product_page(self):
        """Open product page and check product"""
        url = reverse('product', args=[self.product.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test product")

    def test_cart_requires_login(self):
        """Cart page open only for authentication users"""
        url = reverse('order')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_cart_authenticated(self):
        """Authentication user can open the cart page"""
        self.client.login(username="testuser", password="12345678")
        url = reverse('order')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)