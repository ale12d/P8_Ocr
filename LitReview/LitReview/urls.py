from django.contrib import admin
from django.urls import path
from account import views as account_views
from flow import views as flow_views
from reviews import views as reviews_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/login', account_views.login_page),
    path('account/signup', account_views.sign_up_page),
    path('account/logout', account_views.logout_user),

    path('flow/', flow_views.main_flow),
    path('flow/subcription', flow_views.subcription_page),
    path('flow/posts', flow_views.posts_page),

    path('reviews/create', reviews_views.create_review, name ="review"),
    path('reviews/request', reviews_views.request_review, name ="request"),
    
    path('reviews/deleteticket/<int:id>/', reviews_views.delete_ticket, name ="delete-ticket"),
    path('reviews/deletereview/<int:id>/', reviews_views.delete_review, name ="delete-review"),

    path('reviews/modifyticket/<int:id>/', reviews_views.modify_ticket, name ="modify-ticket"),
    path('reviews/modifyreview/<int:id>/', reviews_views.modify_review, name ="modify-review"),
]
