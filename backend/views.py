from django.shortcuts import render
from rest_framework.decorators import api_view
from backend.models import Question,Choice
from rest_framework import status
from rest_framework.response import Response
from .serializers import QuestionSerializer,ChoiceSerializer
from backend import serializers
# Create your views here.

@api_view(['GET'])
def getquestions(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions,many=True)
        return Response(serializer.data)


@api_view(['GET','PUT'])
def getquestion(request,pk):
    if request.method == 'GET':
        question = Question.objects.get(id=pk)
        serializer1 = QuestionSerializer(question,many=False)
        serializer2 = ChoiceSerializer(question.choice_set.all(),many=True)
        return Response({'s1':serializer1.data,'s2':serializer2.data})

    if request.method == 'PUT':
        question = Question.objects.get(id=pk)
        try:
            selected_choice = question.choice_set.get(id=request.data)
        except (KeyError,Choice.DoesNotExist):
            return Response({'msg':'Choice Not Found'},status=status.HTTP_404_NOT_FOUND)
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return Response({'msg':'Success'},status=status.HTTP_200_OK)
        
        
