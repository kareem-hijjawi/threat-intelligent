import time
import requests

while True:
    with open('app.log', 'r') as log_file:
        logs = log_file.read()
    
    # Send logs to MISP or process them as needed
    # For example, sending them as a POST request (assuming MISP endpoint setup)
    response = requests.post('http://localhost:80/events/index', data={'logs': logs})
    print(f"Sent logs to MISP, status code: {response.status_code}")
    
    time.sleep(60)  # Wait for a minute before sending again
