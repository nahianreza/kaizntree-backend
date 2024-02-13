from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Category, Tag, Item
from dashboard.models import Category, Tag

class ItemAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create a category and tags for use in item creation
        self.category = Category.objects.create(name='Test Category')
        self.tag1 = Tag.objects.create(name='Tag1')
        self.tag2 = Tag.objects.create(name='Tag2')

        self.item = Item.objects.create(
        sku='TEST-SKU',
        name='Test Item',
        in_stock=True,
        available_stock=100,
        category=self.category
        )
        self.item.tags.add(self.tag1)

    def test_create_item(self):
        """Test creating a new item via the API"""
        data = {
            'name': 'New Item',
            'sku': 'SKU12345',
            'in_stock': True,
            'available_stock': 100,
            'category': self.category.id,
            'tags': [self.tag1.id, self.tag2.id]
        }
        response = self.client.post('/api/items/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'New Item')

    def test_retrieve_item_list(self):
        """Test retrieving a list of items"""
        response = self.client.get('/api/items/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        url = reverse('item-detail', args=[self.item.id])
        data = {
            'sku': 'UPDATED-SKU',  # Add the 'sku' field
            'name': 'Updated Item Name',
            'in_stock': False,
            'available_stock': 50,
            'category': self.category.id,
            'tags': [self.tag1.id, self.tag2.id]
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, 'Updated Item Name')
        # Add any additional assertions here as needed

    def test_delete_item(self):
        """Test deleting an item"""
        self.assertEqual(Item.objects.count(), 1)  # Ensure there is one item before deletion
        
        # Assuming you have the correct URL pattern
        url = reverse('item-detail', args=[self.item.id])
        response = self.client.delete(url)
        
        # Check the response status code for debugging
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg=response.data)
        
        self.assertEqual(Item.objects.count(), 0)  # Check again after the supposed deletion

class CategoryAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.category = Category.objects.create(name='Initial Category')

    def test_create_category(self):
        """Test creating a new category"""
        response = self.client.post('/api/categories/', {'name': 'New Category'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    def test_list_categories(self):
        """Test listing all categories"""
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming setUp created one category

    def test_update_category(self):
        """Test updating a category"""
        url = f'/api/categories/{self.category.id}/'
        response = self.client.put(url, {'name': 'Updated Category'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, 'Updated Category')

    def test_delete_category(self):
        """Test deleting a category"""
        url = f'/api/categories/{self.category.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

class TagAPITestCase(APITestCase):
    def setUp(self):
    # Create and authenticate the user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Create an initial tag
        self.tag = Tag.objects.create(name='Initial Tag')



    def test_create_tag(self):
        """Test creating a new tag"""
        response = self.client.post('/api/tags/', {'name': 'New Tag'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.count(), 2)

    def test_list_tags(self):
        """Test listing all tags"""
        response = self.client.get('/api/tags/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_tag(self):
        """Test updating a tag"""
        url = f'/api/tags/{self.tag.id}/'
        response = self.client.put(url, {'name': 'Updated Tag'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.name, 'Updated Tag')

    def test_delete_tag(self):
        """Test deleting a tag"""
        url = f'/api/tags/{self.tag.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tag.objects.count(), 0)
