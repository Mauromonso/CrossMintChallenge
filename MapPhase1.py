import requests
import json

# GET request
def get_data():
    url = "https://challenge.crossmint.io/api/map/0d321c9b-f123-47d3-8583-98ec8508833c/goal"  # Get the Map Goal
    response = requests.get(url)
   # print(response.status_code)
    if response.status_code == 200:
        data = response.json()
       # print("GET Response:")
       # print(data)
        first_value = next(iter(data.values()))
        return first_value
    else:
        print("GET Request failed with status code:", response.status_code)
        return None

#  POST request
def post_data(i,j):
    url = "https://challenge.crossmint.io/api/polyanets/"  # Polyanet endpoint
    payload = {
        "row": i,
        "column": j,
        "candidateId": "0d321c9b-f123-47d3-8583-98ec8508833c"
    }

  
    headers = {'Content-Type': 'application/json'}  # Specify Content-Type as JSON
    response = requests.post(url, headers=headers, data=json.dumps(payload))
   # response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        print("POST Response:")
        print(data)
    else:
        print("POST Request failed with status code:", response.status_code)
        print(response.json())

if __name__ == "__main__":
    #We get the map data
   
    GoalMap = get_data()
    if GoalMap:
        print("GET Response:")
        print(GoalMap)
        print("Trying Post")
        # Nested loop to go over the whole matrix
        for idx, fila in enumerate(GoalMap):
            for idx_2, item in enumerate(fila):
                if item == "POLYANET":
                 # send post
                 print("Coordinates for the Polyanet ", idx, idx_2)
                 post_data(idx, idx_2)


 
