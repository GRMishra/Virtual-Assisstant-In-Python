# output in the Text format

# Step 1:
# setx OPENAI_API_KEY "your_api_key_here"  -> run this command on Your Terminak First

#step 2: 

from openai import OpenAI

client = OpenAI(
    api_key = "Your_apikey_here"  # enter your generated api key here
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual asssistant named jarvis skilled in general tasks like alexa and google cloud."},
        {
            "role": "user",
            "content": "What is coding. show the output in plain manner without including escape sequence and bold"
        }
    ]
)

print(completion.choices[0].message.content)