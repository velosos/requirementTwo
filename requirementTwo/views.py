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
        print(url)
        print(description)

        obj= {

            'description':description,
            'short_description':short_description

        }

        objs = json.dumps(obj)

        print(objs)

        user = 'admin'
        pwd = 'Fumaca@01'

        headers = {"Content-Type":"application/json","Accept":"application/json"}

        response = requests.post(url, auth=(user, pwd), headers=headers,data=objs)

        print(response)

        if response.status_code != 200: 
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
            data = response.json()
            
        return render(request, 'record.html', {'data': data})
        
    else:
        form = MyForm()
        return render(request, 'index.html', {'form': form})



def update_record(request):
    if(request.POST):
        dados = request.POST.dict()
        tables = dados.get("table")
        comments = dados.get("comments")
        ids = dados.get("id")

        url = 'https://dev57502.service-now.com/api/now/table/'+str(tables)+'/'+str(ids)
        print(url)
        

        obj= {

            'work_notes':comments,

        }

        objs = json.dumps(obj)

        print("obj segunda view" + objs)

        user = 'admin'
        pwd = 'Fumaca@01'

        headers = {"Content-Type":"application/json","Accept":"application/json"}

        response = requests.put(url, auth=(user, pwd), headers=headers,data=objs)

        print(response)

        if response.status_code != 200: 
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
            data = response.json()
            exit()
            
        return render(request, 'updated.html', {'data': data})
    else:
        
        return render(request, 'test.html',{'form': forms})
    


