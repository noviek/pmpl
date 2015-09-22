from django.shortcuts import render, redirect
from lists.models import Item

def home_page(request):
	#if request.method == 'POST':
	#	Item.objects.create(text=request.POST['item_text'])
	#	return redirect('/lists/the-only-list-in-the-world/')

	#komentar = ""
	#if Item.objects.count() == 0:
	#	komentar = "Yey, waktunya berlibur"
	#elif Item.objects.count() < 5:
	#	komentar = "Sibuk tapi santai"
	#else:
	#	komentar = "Oh tidak"

	#items = Item.objects.all()
	#return render(request, 'home.html', {'items': items, 'komentar': komentar})
	return render(request, 'home.html')

def view_list(request):
	items = Item.objects.all()
	return render(request, 'list.html', {'items': items})

def new_list(request):
	Item.objects.create(text=request.POST['item_text'])
	return redirect('/lists/the-only-list-in-the-world/')
