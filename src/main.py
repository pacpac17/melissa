from stt import stt
from tts import tts
from logic import logic
import json

# Load the profile.json file
with open("profile.json") as f:
    profile = json.load(f)

name = profile["name"]

# tts("Hello " + name + ", I am Melissa. How can I assist you today?")
# userInput = stt()
# print(userInput )



# Pass the name to the logic function
llm_response = logic(f"Hello, my name is {name}")

print("LLM Response:", llm_response
      )
# Pass the response from the logic function to the tts function
tts(llm_response)