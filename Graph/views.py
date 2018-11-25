<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse

def plot(request):
    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    response = HttpResponse(content_type = 'image/png')
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(response)
    return response
=======
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView
import csv

base_dir = '/Users/lawrence/workspace/HackWesternSmartAccount/Graph/templates/'
def csv_upload(request):
	print (request.method)
	if request.method == "GET":
		print('hello')
		return render(request, base_dir + 'csv_upload.html')

	csv_file = request.FILES["csv_file"]
	csv_overwrite(csv_file)
	#file_data = csv_file.read().decode("utf-8")
	return render(request, base_dir + 'jump2.html')

def csv_overwrite(file):
	myFile = open('/Users/lawrence/Desktop/test/test1.csv','w')
	file_data = file.read().decode("utf-8").split('\n')
	for i in range(len(file_data)-1):
		print (file_data[i])
		file_data[i] = file_data[i][:-2].split(',')
		print (file_data[i])
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows(file_data)
	myFile.close()

>>>>>>> 4ab2868c95e8d875a9823a83ec9ddc6717e3ada1
