import requests
import asyncio

# dev_url = "http://172.22.208.99:3003"
dev_url = "http://localhost:3003"
prod_url = "http://91.75.21.130:3003"
    
async def upload_file(file)-> str:
    # The URL endpoint
    url = f"{prod_url}/chatbot/upload_file"

    # The payload to be sent with the POST request
    files = {
        'file': file
    }
    # Making the POST request
    try:
        response = requests.post(url,files=files)
        
        # Check if the request was successful
        if response.status_code == 200:
                # Parse the response JSON 
                return  response.json()["message"]
        else:
            return f"Request failed with status code: {response.status_code}"
    
    except ValueError:
        return "Error: Unable to parse JSON response."
    except requests.Timeout:
        print("The request timed out. Please try again.")
        return "The request timed out. Please try again."
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

async def chat(question):
    # The URL endpoint
    url = f"{prod_url}/chatbot/chat"

    # The payload to be sent with the POST request
    payload = { 
        'query': question
    }

    # Making the POST request
    try:
        response = requests.post(url,data=payload)

        # Check if the request was successful
        return response
    
    except ValueError:
        return "Error: Unable to parse JSON response."
    except requests.Timeout:
        print("The request timed out. Please try again.")
        return "The request timed out. Please try again."
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


async def question_suggestion():
    # The URL endpoint
    url = f"{prod_url}/chatbot/question_suggestion"
    
    # Making the POST request
    try:
        response = requests.get(url)

        # Check if the request was successful
        return response.json()
    
    except ValueError:
        return "Error: Unable to parse JSON response."
    except requests.Timeout:
        print("The request timed out. Please try again.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
  
