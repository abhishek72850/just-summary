from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import watson, utils

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from django.shortcuts import render

# Create your views here.

ai = watson.Watson()


class SummaryAnalysis(APIView):

	def post(self, request, format = None):

		if('content' in request.POST.keys()):
			data = ai.extractSummary(request.POST['content'], True)

			response = utils.BuildResponse(data)

		else:
			response = {
				'status' : status.HTTP_400_BAD_REQUEST,
				'message' : 'Invalid or missing Parameters'
			}

		return Response(response)
