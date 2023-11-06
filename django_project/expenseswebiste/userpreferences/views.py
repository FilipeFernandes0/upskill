from django.shortcuts import render
import os
import json
from django.conf import settings
from .models import UserPreferences
from django.contrib import messages

from django.contrib.auth.decorators import login_required

@login_required(login_url='/authentication/login')
def index(request):
    # Create an empty list to store currency data
    currency_data = []
    # Define the file path for the 'currencies.json' file
    file_path = os.path.join(settings.BASE_DIR, 'currencies.json')
    
    # Open the 'currencies.json' file and load the data
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        # Extract the data from the JSON file and append it to the currency_data list
        for k, v in data.items():
            currency_data.append({'name': k, 'value': v})

    if request.method == 'GET':
        try:
            user_preferences = UserPreferences.objects.get(user=request.user)
            currency = user_preferences.currency
        except UserPreferences.DoesNotExist:
            user_preferences = UserPreferences.objects.create(user=request.user, currency='EUR-EURO')

        return render(request, 'preferences/index.html', {'currencies': currency_data, 'user_preferences': user_preferences})

    if request.method == 'POST':
        exists = UserPreferences.objects.filter(user=request.user).exists()

        if exists:
            user_preferences = UserPreferences.objects.get(user=request.user)
        else:
            user_preferences = UserPreferences.objects.create(user=request.user)

        currency = request.POST.get('currency', None)

        if currency is not None:
            user_preferences.currency = currency
            user_preferences.save()
            messages.success(request, 'Changes saved')
        else:
            messages.error(request, 'Invalid currency value')

        return render(request, 'preferences/index.html', {'currencies': currency_data, 'user_preferences': user_preferences})
