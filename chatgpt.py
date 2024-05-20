import openai

# Configuración de la API de OpenAI
#openai.api_key = 'no la agregue por problemas al hacre commit en github'

# Función para enviar una solicitud de chat a ChatGPT
def enviar_solicitud_chat(mensaje, engine='gpt-3.5-turbo-16k', max_tokens=50, temperatura=0.7):
    respuesta = openai.Completion.create(
        engine=engine,
        prompt=mensaje,
        max_tokens=max_tokens,
        temperature=temperatura
    )
    return respuesta.choices[0].text.strip()

# Función para interactuar con el usuario
def interactuar():
    print("¡Bienvenido al ChatGPT!")
    print("Puedes comenzar a escribir tus mensajes. Escribe 'salir' para terminar la conversación.")
    print("-----------------------------------------")

    # Loop de interacción
    while True:
        mensaje = input("Tu pompt: ")
        
        if mensaje.lower() == 'salir':
            break

        respuesta = enviar_solicitud_chat(mensaje)
        print("ChatGPT: " + respuesta)
        print("-----------------------------------------")

# Ejecutar la función de interacción
interactuar()