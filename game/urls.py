from django.urls import path
from . import views

urlpatterns=[
				path('',views.index,name='index'),
				path('signup/',views.signup,name='signup'),
				path('login/',views.login_view,name='login'),
				path('signout/',views.logout_view,name='logout'),
				path('index2/',views.index2,name = 'index2'),
				path('index2/play/',views.play,name = 'play'),
				path('index2/play/<key>',views.ordering_weapons,name='ordering-weapons'),
				path('index2/play/<key>/confirm',views.ordered_weapons,name='confirm-add'),




			]
			