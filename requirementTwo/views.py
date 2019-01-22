from django.shortcuts import render
import requests
from .forms import MyForm,Update
import json
  
def get_name(request):
    if(request.POST):
        
        dados = request.POST.dict()
        tables = dados.get("tables")
        short_description = dados.get("short_description")
        description = dados.get("description")
        url = 'https://dev57502.service-now.com/api/now/table/'+str(tables)
       
        obj= {

            'description':description,
            'short_description':short_description

        }

        objs = json.dumps(obj)
        user = 'fujitsu.integration'
        pwd = 'fujitsu123'

        headers = {"Content-Type":"application/json","Accept":"application/json"}

        response = requests.post(url, auth=(user, pwd), headers=headers,data=objs)

        if response.status_code != 200: 
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
            data = response.json()
            
        return render(request, 'record.html', {'data': data})
        
    else:
        form = MyForm()
        return render(request, 'index.html', {'form': form})



def update_record(request):
    if(request.POST):

        tables = request.POST.get("table")
        comments = request.POST.get("comments")
        ids = request.POST.get("id")
        numbers = request.POST.get("number")
        print(numbers)

        url = 'https://dev57502.service-now.com/api/now/table/'+str(tables)+'/'+str(ids)
        
        obj= {

            'work_notes':comments,

        }

        objs = json.dumps(obj)
        user = 'fujitsu.integration'
        pwd = 'fujitsu123' 

        headers = {"Content-Type":"application/json","Accept":"application/json"}

        response = requests.put(url, auth=(user, pwd), headers=headers,data=objs)

        print(response)

        if response.status_code != 200: 
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
            data = response.json()
            print(data)            
        return render(request, 'updated.html')
    else:
        
        return render(request, 'record.html')
    
