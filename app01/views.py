from django.shortcuts import render, redirect, HttpResponse
from app01 import models


# Create your views here.

def home(request):
    return render(request, 'home.html')


def booklist(request):
    book_queryset = models.Book.objects.select_related('publish').order_by('pk')
    return render(request, 'booklist.html', locals())


def book_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_time = request.POST.get('publish_time')
        publish_id = request.POST.get('publish_id')
        authors_list = request.POST.getlist('authors_list')
        book_obj=models.Book.objects.create(title=title,
                                   price=price,
                                   publish_time=publish_time,
                                   publish_id=publish_id,
                                   )
        book_obj.authors.add(*authors_list)
        return redirect('app01_booklist_view')
    author_queryset = models.Author.objects.all()
    publish_queryset = models.Publish.objects.all()
    return render(request, 'bookAdd.html', locals())


def book_edit(request,edit_pk):
    edit_obj=models.Book.objects.filter(pk=edit_pk).first()
    author_queryset = models.Author.objects.all()
    publish_queryset = models.Publish.objects.all()
    return render(request, 'bookEdit.html', locals())


def book_del(request,delete_id):
    models.Book.objects.filter(pk=delete_id).delete()
    return redirect('app01_booklist_view')

def ab_ajax(request):
    return render(request,'abajax.html')