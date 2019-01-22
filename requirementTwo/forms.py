from django import forms
import requests


def get_tables():
    url = 'https://dev57502.service-now.com/api/now/table/sys_db_object?sysparm_query=super_class%3D2251f145112023006517efa30493a244'
    user = 'fujitsu.integration'
    pwd = 'fujitsu123'
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers )

    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

    data = response.json()

    choices = data['result']

    tables = []
    for key in choices:
        sys_name = str(key['sys_name'])
        name = str(key['name'])
        tables.append((name,sys_name))
        
    return tables

class MyForm(forms.Form):
    tables = forms.ChoiceField(label='Choose the table',choices=get_tables())
    short_description = forms.CharField(label='Short Description', max_length=100)
    description = forms.CharField(widget=forms.Textarea)

class Update(forms.Form):
    comments = forms.CharField(widget=forms.Textarea)    
