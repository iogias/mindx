from rest_framework.views import APIView
from django.views.generic import TemplateView
from django.views import View
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .models import UnityEmail
from .serializers import UnityEmailSerializer
from django.shortcuts import render
from django.db.models import Q, Count
from django.db.models.functions import TruncMonth
from datetime import date, timedelta


class StoreTemplateViews(TemplateView):
    template_name = 'store.html'


class EmailLeadsListViews(View):
    def get(self, request):
        total_by_month = UnityEmail.objects.annotate(month=TruncMonth(
            'created')).values('month').annotate(total=Count('email'))
        startdate = date.today()
        enddate = startdate + timedelta(days=6)
        # assume new lead is six day from now
        new = UnityEmail.objects.filter(
            created__range=[startdate, enddate])
        status = UnityEmail.objects.filter(status='unsubs').annotate(month=TruncMonth(
            'created')).values('month').annotate(total=Count('email'))

        records = UnityEmail.objects.all().order_by('-created')
        context = {
            'total_by_month': total_by_month[0],
            'new': len(new),
            'status': status[0],
            'records': records
        }
        return render(request, 'leads.html', context)


class UnityEmailList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        if request.method == 'GET':
            emails = UnityEmail.objects.all().order_by('-created')
            serializer = UnityEmailSerializer(emails, many=True)
            if not emails:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        if request.method == 'POST':
            serializer = UnityEmailSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
