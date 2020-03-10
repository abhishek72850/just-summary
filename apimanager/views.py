from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import watson, utils

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
