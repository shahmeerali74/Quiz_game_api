import requests

# Define the URL of your API endpoint
api_url = "http://localhost:8000/api/"

# Send a GET request to the API endpoint
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    api_data = response.json()
    
    # Access the relevant data from the response
    results = api_data.get("results", [])
    
    # Process the results as needed
    for result in results:
        print("Type:", result.get("type"))
        print("Difficulty:", result.get("difficulty"))
        print("Category:", result.get("category"))
        print("Question:", result.get("question"))
        print("Correct Answer:", result.get("correct_answer"))
        print("Incorrect Answers:", result.get("incorrect_answers"))
        print("-------------------------------------")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
