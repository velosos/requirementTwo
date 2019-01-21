from django.shortcuts import render
import requests
from .forms import MyForm

'''
def index(request,template_name="index.html"):

    url = 'https://dev57502.service-now.com/api/now/table/sys_db_object?sysparm_query=super_class%3D2251f145112023006517efa30493a244'

    user = 'admin'
    pwd = ''

    headers = {"Content-Type":"application/json","Accept":"application/json"}

    response = requests.get(url, auth=(user, pwd), headers=headers )

    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

    data = response.json()

    return render(request,template_name,{'obj':data['result']}) 
'''
def create(request, template_name="created.html"):
    data = "Um teste de envio"
    return render(request,template_name,{'data':data})

 

def get_name(request):
    
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
        
            return HttpResponseRedirect('/thanks/')

    else:
        form = MyForm()

    return render(request, 'index.html', {'form': form})