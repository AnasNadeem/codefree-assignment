from django.urls import path
from iris_assignment_app.views import IrisCreateView, IrisDeleteView

urlpatterns = [
    # path('list-all/', IrisListView.as_view()),
    path('iris/', IrisCreateView.as_view()),
    path('del-iris/<int:pk>/', IrisDeleteView.as_view()),
]
