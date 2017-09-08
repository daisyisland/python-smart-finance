import urllib.request
# If you are using Python 3+, import urllib instead of urllib2

import json 

import sys

data =  {
                "Inputs": {
                    "input1": {
                    "ColumnNames": [
                        "age",
                        "workclass",
                        "fnlwgt",
                        "education",
                        "education-num",
                        "marital-status",
                        "occupation",
                        "relationship",
                        "race",
                        "sex",
                        "capital-gain",
                        "capital-loss",
                        "hours-per-week",
                        "native-country"
                    ],
                    "Values": [
                        [
                        "39",
                        "State-gov",
                        "77516",
                        "Bachelors",
                        "13",
                        "Never-married",
                        "Adm-clerical",
                        "Not-in-family",
                        "White",
                        "Male",
                        "2174",
                        "0",
                        "40",
                        "United-States"
                        ]
                    ]
                    }
                },
                "GlobalParameters": {}
            }


def post_azure(data_input):
    
    data = data_input 

    body = str.encode(json.dumps(data))


    url = 'https://ussouthcentral.services.azureml.net/workspaces/5e798bc5091b49228aae3eeade6cdbe3/services/a11b2e5795ab444bafda82c0f11447f2/execute?api-version=2.0&details=true'
    api_key = 'uxggw0o98vz9WS+/2ou3jJfNxvvLG3iTUaVFK9hc40ZW9DzemTlpD0J9ma+KwpwpqhiXBTR5L5GR6G49RLqtzQ==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers) 
        # response = urllib.request.urlopen(req)

        result = response.read()
        print(result) 
        sys.stdout.flush()

    except urllib2.HTTPError.error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))  
        
