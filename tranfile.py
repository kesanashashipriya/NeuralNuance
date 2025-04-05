# import requests

# TWILIO_ACCOUNT_SID = "AC645863252fbe5b26771da38d51535391"
# TWILIO_AUTH_TOKEN = "d5e419c3e11e031abd732c14253dfca8"

# def download_twilio_recording(recording_url):
#     """
#     Downloads Twilio recording and saves it locally.
#     """
#     response = requests.get(recording_url, auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN))
    
#     if response.status_code == 200:
#         with open("recording.wav", "wb") as f:
#             f.write(response.content)
#         print("Recording downloaded successfully.")
#         return "recording.wav"  # Return local file path
#     else:
#         print(f"Failed to download recording. Status Code: {response.status_code}")
#         return None
