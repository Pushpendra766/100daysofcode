import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USER = "Your username"
TOKEN = "your token"
pixela_paramas = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=pixela_paramas)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"
graph_params = {
    "id":"graph1",
    "name":"Exercise graph",
    "unit":"Min",
    "type":"int",
    "color":"momiji",
}
headers = {
    "X-USER-TOKEN":TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
today = datetime.now()
pixel_endpoint = f"{graph_endpoint}/graph1"
pixel_params = {
    "date":today.strftime("%Y%m%d"),
    "quantity": input("How many minutes do you exercised today ? "),
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

update_pixel_endpoint = f'{pixel_endpoint}/{today.strftime("%Y%m%d")}'
update_params = {
    "quantity": "10",
}
# response = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
# print(response.text)

# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response.text)
