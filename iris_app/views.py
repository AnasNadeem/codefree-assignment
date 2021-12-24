from django.shortcuts import render
from iris_assignment_app.models import Iris
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    if request.method=='POST':
        sepal_length = request.POST.get('sepalLength')
        sepal_width = request.POST.get('sepalWidth')
        petal_length = request.POST.get('petalLength')
        petal_width = request.POST.get('petalWidth')
        iris_class = request.POST.get('irisClass')
        # Storing it in the database 
        iris = Iris()
        iris.sepal_length = sepal_length
        iris.sepal_width = sepal_width
        iris.petal_length = petal_length
        iris.petal_width = petal_width
        iris.iris_class = iris_class
        iris.save()
        messages.info(request, f"Iris data created.")
    return render(request, 'index.html')