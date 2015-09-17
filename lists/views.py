from django.shortcuts import render, redirect
from lists.models import Item

def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/')

	komentar = ""
	if Item.objects.count() == 0:
		komentar = "Yey, waktunya berlibur"
	elif Item.objects.count() < 5:
		komentar = "Sibuk tapi santai"
	else:
		komentar = "Oh tidak"

	items = Item.objects.all()
	return render(request, 'home.html', {'items': items, 'komentar': komentar})
	
