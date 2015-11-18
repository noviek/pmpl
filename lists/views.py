from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
	komentar = "Yey, waktunya berlibur"
	return render(request, 'home.html', {'komentar': komentar})

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	count_list = Item.objects.filter(list_id=list_id).count()
	error = None
	komentar = ""

	if request.method == 'POST':
		try:
			item = Item(text=request.POST['item_text'], list=list_)
			item.full_clean()
			item.save()
			return redirect(list_)
		except ValidationError:
			error = "You can't have an empty list item"

	if count_list == 0:
		komentar = "Yey, waktunya berlibur"
	elif count_list < 5:
		komentar = "Sibuk tapi santai"
	else:
		komentar = "Oh tidak"
	return render(request, 'list.html', {'komentar': komentar, 'list': list_, 'error': error})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html', {"error", error})
	return redirect(list_)

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))
	
