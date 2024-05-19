import requests

url = "http://127.0.0.1:81/"  # Replace this with the URL of your login page

# Define a list of usernames and passwords to try
usernames = ["user1", "user2", "user3"]
passwords = ["password1", "password2", "password3"]

# Loop through each username and password combination
for username in usernames:
    for password in passwords:
        # Define the form data including the honeypot field
        form_data = {
            "username": username,
            "password": password,
            "honeypot": "botnet"
        }

        # Send a POST request with the form data
        response = requests.post(url, data=form_data)
        
        

        # Check the response
        if response.status_code == 200:
            print(f"Login Successful! Username: {username}, Password: {password}")
        else:
            print(f"Login Failed for Username: {username}, Password: {password}. Status Code:", response.status_code)

