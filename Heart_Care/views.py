from django.shortcuts import render
import pickle
# Create your views here.

def home(request):
	return render(request, 'home.html')

def services(request):
	return render(request, 'services.html')

def doctors(request):
	return render(request, 'doctors.html')

def results(request):
	age = request.POST['age']
	sex = request.POST['sex']
	cp = request.POST['cp']
	if cp == 'Typical Angina':
		cp_pred = 0
	elif cp == 'Atypical Angina':
		cp_pred = 1
	elif cp == 'Non-Angina':
		cp_pred = 2
	elif cp == 'Asymptomatic':
		cp_pred = 3

	restecg_pred = request.POST['restecg']
	thalach_pred = request.POST['thalach']
	slope_pred = request.POST['slope']
	chol_pred = request.POST['chol']
	fbs = request.POST['fbs']

	if fbs == 'No':
		fbs_pred = 0
	elif fbs == 'Yes':
		fbs_pred = 1

	user_input = [[cp_pred,restecg_pred,thalach_pred,slope_pred,chol_pred,fbs_pred]]

	with open('model.pickle', 'rb') as f:
		model = pickle.load(f)

	percentage = model.predict_proba(user_input)
	percentage = percentage[0][1]
	
	percentage = percentage * 100

	percentage = "{:.2f}".format(percentage)
	
	results_dict = {}
	results_dict['age'] = age
	results_dict['sex'] = sex
	results_dict['cp'] = cp
	results_dict['restecg'] = restecg_pred
	results_dict['thalach'] = thalach_pred
	results_dict['slope'] = slope_pred
	results_dict['chol'] = chol_pred
	results_dict['fbs'] = fbs
	results_dict['percentage'] = percentage
	return render(request,'results.html',results_dict)




