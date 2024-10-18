from django.urls import path

from humans.views import (HumanCreateView, HumanDeleteView,
                          HumanPrepareUpdateView, HumanTask1ListView,
                          HumanTask1PrepareView, HumanTask2ListView,
                          HumanTask2PrepareView, HumanUpdateView, Index)

app_name = 'humans'

urlpatterns = [
    path('create/', HumanCreateView.as_view(), name='create'),

    path('update/', HumanPrepareUpdateView.as_view(), name='update_prepare'),
    path('update/<int:id>/', HumanUpdateView.as_view(), name='update'),

    path('delete/<int:id>/', HumanDeleteView.as_view(), name='delete'),

    path('task-1/', HumanTask1PrepareView.as_view(), name='task_1_prepare'),
    path('task-1/<int:id>/', HumanTask1ListView.as_view(), name='task_1'),

    path('task-2/', HumanTask2PrepareView.as_view(), name='task_2_prepare'),
    path('task-2/<int:id>/', HumanTask2ListView.as_view(), name='task_2'),

    path('', Index.as_view(), name='index'),
]
