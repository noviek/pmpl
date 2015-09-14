from django.http import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse

def home_page(request):
	#if request.method == 'POST':
	#	return HttpResponse(request.POST['item_text'])
	return render(request, 'home.html', {
		'new_item_text': request.POST.get('item_text', ''),
	})
	#return HttpResponse('<html><title>Novie Kamalia - 1206239806</title><body>Hello, Novie Kamalia (1206239806)</body></html>')
	
