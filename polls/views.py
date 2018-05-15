from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from .models import Stock
from .serializers import stockSerializer


# Lists all stock or creates a new one
# stocks/
class StockList(APIView):

    def get(self, request):
        stocks= Stock.objects.all()
        serializer = stockSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self):
        pass



# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of the question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

