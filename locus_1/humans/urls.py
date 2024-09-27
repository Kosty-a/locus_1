from django.urls import path

from .views import HumanCreateView, HumanListView, HumanTask1View, HumanTask2View


app_name = 'humans'

urlpatterns = [
    path('create/', HumanCreateView.as_view(),
         name='create_human'),
    path('task-1/<int:id>/', HumanTask1View.as_view()),
    path('task-2/<int:id>/', HumanTask2View.as_view()),
    path('', HumanListView.as_view(), name='list_human'),
]
