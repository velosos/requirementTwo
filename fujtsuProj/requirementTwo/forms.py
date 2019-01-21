from django import forms
import requests


def get_my_choices():
    url = 'https://dev57502.service-now.com/api/now/table/sys_db_object?sysparm_query=super_class%3D2251f145112023006517efa30493a244'
    user = 'admin'
    pwd = ''
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers )

    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

    data = response.json()

    choices = data['result']

    users = []
    for key  in choices:
        users.append(str(key['name']))
   
    print(users)
    return users

class MyForm(forms.Form):
    my_choice_field = forms.ChoiceField(choices=get_my_choices())
