import requests
import json
import time

#  GET request to get the Map Goal
def get_data():
    url = "https://challenge.crossmint.io/api/map/0d321c9b-f123-47d3-8583-98ec8508833c/goal"  # Get the Map Goal
    response = requests.get(url)
   # print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        first_value = next(iter(data.values())) # we need to parse the JSON and get the matrix
        return first_value
    else:
        print("GET Request failed with status code:", response.status_code)
        return None

#  POST request Polyanets
def post_Polyanets(i,j):
    url = "https://challenge.crossmint.io/api/polyanets/"  # Polyanets endpoint
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
# Post Soloons
def post_Soloons(i,j,color):
    url = "https://challenge.crossmint.io/api/soloons/"  # Soloons endpoint
    payload = {
        "row": i,
        "column": j,
        "candidateId": "0d321c9b-f123-47d3-8583-98ec8508833c",
        "color": color
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

# Post Cometh
def post_Cometh(i,j,direction):
    url = "https://challenge.crossmint.io/api/comeths/"  # Cometh endpoint
    payload = {
        "row": i,
        "column": j,
        "candidateId": "0d321c9b-f123-47d3-8583-98ec8508833c",
        "direction": direction
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
        #post_data(1,1)
        for idx, fila in enumerate(GoalMap):
            for idx_2, item in enumerate(fila):
                if "POLYANET" in item:
                 # send post
                    print("Coordinates for the Polyanet ", idx, idx_2)
                
                    post_Polyanets(idx, idx_2)
                    time.sleep(2) # We wait 2 seconds to prevent server side clogging
                
                if "COMETH" in item:
                    direction, _ = item.split("_")
                    direction = direction.lower()
                    print("Coordinates for the Cometh ", idx, idx_2, direction)
                    post_Cometh(idx,idx_2,direction)
                    time.sleep(2) # We wait 2 seconds to prevent server side clogging
                if "SOLOON" in item:
                    color, _ = item.split("_")
                    color = color.lower()
                    print("Coordinates for the Soloon ", idx, idx_2, color)
                    post_Soloons(idx,idx_2,color)
                    time.sleep(2) # We wait 2 seconds to prevent server side clogging
     





 
