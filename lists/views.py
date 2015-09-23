from django.shortcuts import render, redirect
from lists.models import Item, List

def home_page(request):
	#if request.method == 'POST':
	#	Item.objects.create(text=request.POST['item_text'])
	#	return redirect('/lists/the-only-list-in-the-world/')

	komentar = "Yey, waktunya berlibur"
	#if Item.objects.count() == 0:
	#	komentar = "Yey, waktunya berlibur"
	#elif Item.objects.count() < 5:
	#	komentar = "Sibuk tapi santai"
	#else:
	#	komentar = "Oh tidak"

	#items = Item.objects.all()
	return render(request, 'home.html', {'komentar': komentar})
	#return render(request, 'home.html')

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	#items = Item.objects.filter(list=list_)
	#return render(request, 'list.html', {'items': items})
	count_list = Item.objects.filter(list_id=list_id).count()

	komentar = ""
	if count_list == 0:
	#if Item.objects.count() == 0:
		komentar = "Yey, waktunya berlibur"
	elif count_list < 5:
	#elif Item.objects.count() < 5:
		komentar = "Sibuk tapi santai"
	else:
		komentar = "Oh tidak"

	return render(request, 'list.html', {'komentar': komentar, 'list': list_})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	#return redirect('/lists/the-only-list-in-the-world/')
	return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))
	
