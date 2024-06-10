from django.urls import path
from webapp import views

# name in the http title, views.function name, name given in the html page as url.
urlpatterns = [
    path('', views.home_pg, name="home_pg"),
    path('about', views.about_pg, name="about_pg"),
    path('contact_pg/', views.contact_pg, name="contact_pg"),
    path('save_contact/', views.save_contact, name="save_contact"),
    path('shope_pg/', views.shope_pg, name="shope_pg"),
    path('filtered_products_pg/<P_catname_id>/', views.filtered_products_pg, name="filtered_products_pg"),
    path('single_product_pg/<int:Pid>/', views.single_product_pg, name="single_product_pg"),
    path('registration_pg/', views.registration_pg, name="registration_pg"),
    path('save_registration_signUp/', views.save_registration_signUp, name="save_registration_signUp"),
    path('UserLogin_su/', views.UserLogin_su, name="UserLogin_su"),
    path('UserLogout_su/', views.UserLogout_su, name="UserLogout_su"),
    path('save_cart/', views.save_cart, name="save_cart"),
    path('cart_pg/', views.cart_pg, name="cart_pg"),
    path('delete_cartitem/<int:Dcid>/', views.delete_cartitem, name="delete_cartitem"),
    path('checkout_Pg/', views.checkout_Pg, name="checkout_Pg"),
    path('payment_pg/', views.payment_pg, name="payment_pg"),
    path('save_checkout/', views.save_checkout, name="save_checkout"),
]