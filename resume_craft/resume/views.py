from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResumeJObSerializer
from .script import craft_resume
# Create your views here.
def home(request):
    return render(request,'resume/home.html')

class ResumeJobAPIView(APIView):
    def post(self,request):
        serializer=ResumeJObSerializer(data=request.data)
        if serializer.is_valid():
            latex_resume=serializer.validated_data['latex_resume']
            job_description=serializer.validated_data['job_description']
            output=craft_resume(latex=latex_resume,Job_desc=job_description)
            print(output)

            return Response({
                'message':'Resume and Job Description received successfully',
                'latex_resume':output,
            },
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    