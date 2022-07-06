# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from base.models import StudentData
from .serializers import StudentDataSerializer
from rest_framework.permissions import IsAuthenticated


class StudentApiView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        studentdata = StudentData.objects.all()
        serializer = StudentDataSerializer(studentdata, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
