import openai

openai.api_key = 'API_KEY_ANDA'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # atau engine lain sesuai dengan model yang Anda pilih
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

user_input = input("Masukkan pertanyaan: ")
print(chat_with_gpt(user_input))
