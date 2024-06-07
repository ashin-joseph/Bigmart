from django.urls import path
from backend import views

urlpatterns = [
    path('admin_pg/',views.admin_pg, name="admin_pg"),
    path('admin_login/',views.admin_login, name="admin_login"),
    path('admin_logout/',views.admin_logout, name="admin_logout"),
# ********************************************************************************************************
    path('index_pg/',views.index_pg, name="index_pg"),
    path('add_category_pg/',views.add_category_pg, name="add_category_pg"),
    path('save_ac/',views.save_ac, name="save_ac"),
    path('display_pg/',views.display_pg, name="display_pg"),
    path('edit_pg/<int:Eid>/',views.edit_pg, name="edit_pg"),
    path('update_ac/<int:Uid>/',views.update_ac, name="update_ac"),
    path('delete_ac/<int:Did>/',views.delete_ac, name="delete_ac"),
#*********************************************************************************************************
    path('add_product_pg/',views.product_pg, name="add_product_pg"),
    path('save_product/',views.save_product, name="save_product"),
    path('P_display_pg/',views.P_display_pg, name="P_display_pg"),
    path('P_edit_pg/<int:EPid>/',views.P_edit_pg, name="P_edit_pg"),
    path('P_update/<int:UPid>/',views.P_update, name="P_update"),
    path('P_delete/<int:DPid>/',views.P_delete, name="P_delete"),
#******************************************************************************************************
    path('contact_display_wa/', views.contact_display_wa, name="contact_display_wa"),
    path('delete_contact/<int:DCtid>/', views.delete_contact, name="delete_contact"),
]
