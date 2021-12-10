from django.shortcuts import render, redirect
import os
import numpy as np
import joblib as joblib
from sklearn import linear_model
# Create your views here.

def index(request):
    return render(request, 'forecast/index.html')


def prediction(request):
    if request.method == 'POST':
        day = request.POST['day']
        dayofweek = request.POST['dayofweek']
        month = request.POST['month']

        day = int(day)
        dayofweek = int(dayofweek)
        month = int(month)

        data = [day, dayofweek, month]
        data = np.array(data)
        data = np.array(data).reshape(1,-1)

        directory = 'F:/PYCHARM/DJANGO/udemy/forecast/model'
        model = os.path.join(directory, 'rogreg.pkl')
        model = joblib.load(model)
        prediction = model.predict(data)
        prediction = prediction[0]

        context = {'prediction': prediction}
        return render(request, 'forecast/index.html', context)
    else:
        return redirect('home')

