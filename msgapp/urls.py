from django.urls import path
from msgapp import views
from msgapp.views import ContactFrom

urlpatterns = [
    #path('urlpatter',views.fun_name)
    #path('urlpatter',classbane.as_view())
    path('about',views.about),
    path("delete/<eid>",views.delete),
    path('classbase/<eid>',ContactFrom.as_view()),
    path('hello',views.hello),
    #path('gm',views.gm)
    path('main',views.main),
    path('product',views.product),
    path('cart',views.cart),
    path('gm',views.gm),
    path('dashboard',views.dashboard),
    path('edit/<eid>',views.edit),



]
