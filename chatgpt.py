import openai

openai.api_key = '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'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # atau engine lain sesuai dengan model yang Anda pilih
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

user_input = input("Masukkan pertanyaan: ")
print(chat_with_gpt(user_input))
