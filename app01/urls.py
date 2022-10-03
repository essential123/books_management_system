from django.urls import path
from app01 import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('home/', views.home),
#     path('booklist/', views.booklist),
#     path('authorlist/', views.authorlist),
#     path('publishlist/', views.publishlist),
# ]

urlpatterns = [
    # 首页
    path('home/', views.home, name='app01_home_view'),
    # 书籍展示页
    path('booklist/', views.booklist, name='app01_booklist_view'),
    # 书籍添加页
    path('bookAdd/', views.book_add, name='app01_book_add_view'),
    # 书籍修改页
    path('bookEdit/<int:edit_pk>/', views.book_edit, name='app01_book_edit_view'),
    # 书籍删除
    path('bookDel/', views.book_del, name='app01_book_del_view'),
    # ajax的基本使用
    path('abAjax',views.ab_ajax)
]

