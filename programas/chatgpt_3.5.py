import openai

openai.api_key = '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'

modelo = 'gpt-3.5-turbo'
prompt = input("¿Cuál es su consulta?: ")
contexto = input("¿Qué contexto quiere darle a la consulta?: ")

mensajes = [
    {'role': 'system', 'content': contexto},
    {'role': 'user','content':prompt}
]

respuesta = openai.ChatCompletion.create(
    model = modelo,
    messages = mensajes,
    temperature = 0.8,
    max_tokens = 1000
)

print(respuesta['choices'][0]['message']['content'])