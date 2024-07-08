# app1/tests/test_views.py

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from django.contrib.auth.models import Permission

@pytest.mark.django_db
def test_index_view():
    client = Client()
    url = reverse('index')  
    response = client.get(url)
    assert response.status_code == 200
    assert "content/initialBody.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_about_view():
    client = Client()
    url = reverse('about')  
    response = client.get(url)
    assert response.status_code == 200
    assert "content/about.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_ensamblador_view():
    client = Client()
    url = reverse('ensamblador')  
    response = client.get(url)
    assert response.status_code == 200
    assert "content/ensamblador.html" in [t.name for t in response.templates]
    assert 'is_authenticated' in response.context

@pytest.mark.django_db
def test_configuraciones_view_requires_login():
    client = Client()
    url = reverse('configuraciones')  
    response = client.get(url)
    assert response.status_code == 302  
    assert response.url.startswith('/accounts/login/')

@pytest.mark.django_db
def test_configuraciones_view_logged_in():
    client = Client()
    user = User.objects.create_user(username='testuser', password='12345')
    client.login(username='testuser', password='12345')
    url = reverse('configuraciones')  
    response = client.get(url)
    assert response.status_code == 200
    assert "content/configuraciones.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_DatosUsuario_view_requires_login():
    client = Client()
    url = reverse('DatosUsuario') 
    response = client.get(url)
    assert response.status_code == 302  
    assert response.url.startswith('/accounts/login/')

@pytest.mark.django_db
def test_DatosUsuario_view_logged_in():
    client = Client()
    user = User.objects.create_user(username='testuser', first_name='Test', last_name='User', email='test@example.com', password='12345')
    client.login(username='testuser', password='12345')
    url = reverse('DatosUsuario') 
    response = client.get(url)
    assert response.status_code == 200
    assert "content/DatosUsuario.html" in [t.name for t in response.templates]
    assert response.context['username'] == 'testuser'
    assert response.context['first_name'] == 'Test'
    assert response.context['last_name'] == 'User'
    assert response.context['email'] == 'test@example.com'

@pytest.mark.django_db
def test_panelControl_view_requires_staff():
    client = Client()
    user = User.objects.create_user(username='testuser', password='12345')
    client.login(username='testuser', password='12345')
    url = reverse('panelControl')  
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_panelControl_view_as_staff():
    client = Client()
    user = User.objects.create_user(username='teststaff', password='12345', is_staff=True)
    client.login(username='teststaff', password='12345')
    url = reverse('panelControl')  
    response = client.get(url)
    assert response.status_code == 200
    assert "content/panelControl.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_Contactar_view_get():
    client = Client()
    url = reverse('Contactar') 
    response = client.get(url)
    assert response.status_code == 200
    assert "content/Contactar.html" in [t.name for t in response.templates]
    assert 'form' in response.context

@pytest.mark.django_db
def test_Contactar_view_post_valid():
    client = Client()
    url = reverse('Contactar')  
    data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@example.com',
        'country': 'CA',
        'phone_number': '1234567890',
        'message': 'Test message',
        'agree_to_policies': True
    }
    response = client.post(url, data)
    assert response.status_code == 302  
    assert response.url == reverse('index')

@pytest.mark.django_db
def test_Contactar_view_post_invalid():
    client = Client()
    url = reverse('Contactar')  
    data = {
        'first_name': '',
        'last_name': 'Doe',
        'email': 'john@example.com',
        'country': 'Country',
        'phone_number': '1234567890',
        'message': 'Test message',
        'agree_to_policies': True
    }
    response = client.post(url, data)
    assert response.status_code == 200 
    assert "content/Contactar.html" in [t.name for t in response.templates]
    assert 'form' in response.context
    assert response.context['message'] == 'Error: Por favor, revisa los campos esten completos.'

@pytest.mark.django_db
def test_Incidencias_view_requires_staff():
    client = Client()
    user = User.objects.create_user(username='testuser', password='12345')
    client.login(username='testuser', password='12345')
    url = reverse('Incidencias')  
    response = client.get(url)
    assert response.status_code == 302  

@pytest.mark.django_db
def test_Incidencias_view_as_staff():
    client = Client()
    user = User.objects.create_user(username='teststaff', password='12345', is_staff=True)
    client.login(username='teststaff', password='12345')
    url = reverse('Incidencias') 
    response = client.get(url)
    assert response.status_code == 200
    assert "content/incidencias.html" in [t.name for t in response.templates]
