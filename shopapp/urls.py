from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'shopapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    #path(
    #     'Shop-detail/<int:pk>/',
    #     views.Shop_detail,
    #     name = 'Shop_detail',
    #     ),
    path('post/', views.CreateShopView.as_view(), name='post'),
    path('shop/<category>', views.CategoryView.as_view(), name='shop_category'),
    path('contact',views.ContactView.as_view(),name='contact'),
    path('bookmark/<int:product_id>/', views.toggle_bookmark, name='toggle_bookmark'),
    path('buy/', views.CreateShopView.as_view(), name='buy'),
    path('bookmarked_list/', views.bookmark_list, name='bookmark_list'),
    path('mypage/',views.MypageView.as_view(), name='mypage'),
    path('shop_detail/<int:pk>',views.DetailView.as_view(),name = 'shop_detail'),
    path('user-list/<user>',views.UserView.as_view(),name = 'user_list'),
    path('purchase/<int:id>/', views.PurchaseView.as_view(), name='shop_purchase'),
    path('purchase/confirm/<int:id>/', views.PurchaseConfirmView.as_view(), name='purchase_confirm'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
