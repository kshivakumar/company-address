"""Views"""

from collections import defaultdict

from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CompanyAddress
from .serializers import CompanyAddressSerializer


class AddressList(APIView):

    def get(self, _request):
        snippets = CompanyAddress.objects.all()
        serializer = CompanyAddressSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanyAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddressDetail(APIView):

    def get_object(self, pk):
        try:
            return CompanyAddress.objects.get(pk=pk)
        except CompanyAddress.DoesNotExist:
            raise Http404

    def get(self, _request, pk):
        address = self.get_object(pk)
        serializer = CompanyAddressSerializer(address)
        return Response(serializer.data)

    def put(self, request, pk):
        address = self.get_object(pk)
        serializer = CompanyAddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, _request, pk):
        address = self.get_object(pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_addresses_of_company(_request, company):
    address = CompanyAddress.objects.filter(company_name__iexact=company)
    serializer = CompanyAddressSerializer(address, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_companies_in_city(_request, city):
    address = CompanyAddress.objects.filter(city__iexact=city)
    companies = address.values_list('company_name').distinct()
    companies = [c[0] for c in companies]
    return Response({city: list(companies)})


@api_view(['GET'])
def get_postal_codes(request):
    no_of_companies = \
        int(request.query_params.get('companiesCountGreaterThan'))
    codes_companies = \
        CompanyAddress.objects.all().values_list('postal_code', 'company_name')

    dd = defaultdict(set)
    for postal_code, company_name in codes_companies:
        dd[postal_code].add(company_name)

    required_postalcodes = {}
    for postal_code, companies in dd.items():
        if len(companies) > no_of_companies:
            required_postalcodes[postal_code] = companies

    return Response(required_postalcodes)
