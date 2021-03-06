from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    path('update/<str:id>', views.provider_update_equip),
    path('on/<str:id>',views.provider_on_equip),
    path('off/<str:id>', views.provider_off_equip),
    path('super_on_equip/<str:id>',views.super_on_equip),
    path('equip/<int:id>/', views.equip),
    path('deny/', views.deny_equip),
    path('cancel_waitlist/', views.cancel_waitlist),
    path('waitlist/',views.user_to_waitinglist),
    path('rentlist/', views.equip_rent_list),
    path('rentlist/<str:id>', views.equip_rent_list_specific),
    path('rentdescription/',views.equip_borrow_user_info),
    path('equip_history/',views.equip_history),
    path('accept_rent_apply/',views.accept_rent_equip),
    path('accept_rent_deny/',views.deny_rent_equip),
    path('delete/', views.provider_del_equip),
    path('equiplist/',views.equip_list),
    path('equiponlist/',views.equip_on_list),
    path('description/',views.super_view_apply_equip_info),
    path('return_equip/',views.return_equip),
    path('return_equip_check/',views.return_equip_check),
    path('view_wait/',views.equip_waiting_list),
    path('wujun_is/', views.wujun_is),
    path('wait_allow/',views.super_allow_equip_rent),
    path('equip_grade/', views.equip_grading),


]