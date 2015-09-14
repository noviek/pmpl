from django.shortcuts import render
# from django.http import HttpResponse

def home_page(request):
	return render(request, 'home.html')
	#return HttpResponse('<html><title>Novie Kamalia - 1206239806</title><body>Hello, Novie Kamalia (1206239806)</body></html>')
	
