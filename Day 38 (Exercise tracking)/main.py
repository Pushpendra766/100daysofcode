import requests
from datetime import datetime
import os
GENDER = "male"
WEIGHT_KG = "62"
HEIGHT_CM = "178"
AGE = "19"
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
exercise_endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me what you have done today ?")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
params = {
    "query": exercise_text,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE,
}
today = datetime.now()
response = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = response.json()
for exercise in result['exercises']:
    exercise_name = exercise['name'].title()
    exercise_duration = exercise['duration_min']
    calories = exercise['nf_calories']

    sheety_endpoint = os.environ["SHEET_ENDPOINT"]
    sheety_params = {
        "workout":{
            "date":today.strftime("%d/%m/%Y"),
            "time":today.strftime("%X"),
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": calories,
        }
    }
    response = requests.post(
        url=sheety_endpoint,
        json=sheety_params,
        auth=(
            os.environ["USERNAME"],
            os.environ.get('PASSWORD'),
        )
    )
    print(response.text)