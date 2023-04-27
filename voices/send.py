import requests

# Set the URL of the server
url = 'http://localhost:8000'

# Define the command to be sent to the server
command = {'command': 'execute_script'}

# Send a POST request to the server with the command payload
response = requests.post(url, data=command)

# Print the response from the server
print(response.text)
