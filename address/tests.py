"""Unit Tests"""

from rest_framework.test import APITestCase

from .models import CompanyAddress


def generic_setup():
    CompanyAddress.objects.create(
        company_name='Company 1',
        building_number='BN1',
        postal_code='111-222',
        locality='Locality 1',
        city='City 1',
        state='State 1'
    )

    CompanyAddress.objects.create(
        company_name='Company 2',
        building_number='BN2',
        postal_code='333-444',
        locality='Locality 2',
        city='City 2',
        state='State 2'
    )

    CompanyAddress.objects.create(
        company_name='Company 3',
        building_number='BN3',
        postal_code='333-444',
        locality='Locality 2',
        city='City 2',
        state='State 2'
    )


class AddressListTest(APITestCase):

    def setUp(self):
        generic_setup()

    def test_get(self):
        response = self.client.get('/address/')
        assert len(response.data) == 3
        assert response.data[1]['company_name'] == 'Company 2'

    def test_post(self):
        payload = {
            'company_name': 'Company 4',
            'building_number': 'BN4',
            'postal_code': '555-666',
            'locality': 'Locality 4',
            'city': 'City 4',
            'state': 'State 4'
        }
        response = self.client.post('/address/', data=payload, format='json')
        assert response.status_code == 201


class AddressDetailTest(APITestCase):

    def setUp(self):
        generic_setup()

    def test_get(self):
        response = self.client.get('/address/1/')
        assert response.data['postal_code'] == '111-222'

    def test_get_error(self):
        response = self.client.get('/address/25/')
        assert response.status_code == 404

    def test_put(self):
        payload = {
            'company_name': 'Company 1',
            'building_number': 'BN100',
            'postal_code': '111-222',
            'locality': 'Locality 1',
            'city': 'City 1',
            'state': 'State 1',
        }
        response = self.client.put('/address/1/', data=payload, format='json')
        assert response.data['building_number'] == 'BN100'
        assert CompanyAddress.objects.count() == 3

    def test_put_error(self):
        payload = {
            'cool': 'buddy'
        }
        response = self.client.put('/address/1/', data=payload, format='json')
        assert response.status_code == 400

    def test_delete(self):
        _ = self.client.delete('/address/2/')
        assert CompanyAddress.objects.count() == 2


class FunctionViewsTest(APITestCase):

    def setUp(self):
        generic_setup()

    def test_get_addresses_of_company(self):
        response = self.client.get('/address/company/Company 1/')
        assert response.data[0]['id'] == 1

    def test_get_companies_in_city(self):
        response = self.client.get('/address/city/City 1/')
        assert len(response.data['City 1']) == 1

    def test_get_postal_codes(self):
        response = self.client.get(
            '/address/getPostalCodes?companiesCountGreaterThan=1')
        assert response.data == {'333-444': {'Company 2', 'Company 3'}}
