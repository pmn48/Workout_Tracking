import requests, os
from datetime import datetime

# Personal Info
APP_ID = os.environ.get("MY_ID")
APP_KEY = os.environ.get("MY_KEY")
GENDER = #"male" or "female"
WEIGHT = #your_weight_in_kg
HEIGHT = #your_height_in_cm
AGE = #your_age_in_years

# The NutrioniX API that takes query as input and returns exercise type and calories burned
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}
parameter = {
    "query": input("How did you exercise today? "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}
response = requests.post(url=exercise_endpoint, json=parameter, headers=header)
res = response.json()


# The Sheety API that takes the json input into a Google sheet for tracking
def entry_ggsheet(result: dict):
    for ex in result['exercises']:
        new_dict = {
            'workout': {
                "date": today.date().strftime("%d/%m/%Y"),
                "time": today.time().strftime("%H:%M:%S"),
                "exercise": ex['name'].title(),
                "duration": ex['duration_min'],
                "calories": ex['nf_calories']
            }
        }
        rrequest = requests.post(url=sheety_endpoint, json=new_dict, headers=s_header)


param_list = ['name', 'duration_min', 'nf_calories']
today = datetime.now()

sheety_endpoint = "https://api.sheety.co/16ffe0a69af93fb50fdb8108b1d365f0/myWorkouts/workouts"
s_header = {
    'Authorization': f'Bearer {os.environ.get("S_TOKEN")}'
}

entry_ggsheet(res)
