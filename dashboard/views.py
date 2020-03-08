from django.shortcuts import render

# Create your views here.


def text_summary(request):
	return render(request, 'dashboard/summary.html')
