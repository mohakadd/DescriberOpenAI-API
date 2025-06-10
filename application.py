import time
import os
import requests
from openai import OpenAI

# Définir la clé API OpenAI
OpenAI.api_key = os.getenv('OPENAI_API_KEY')
api_key = OpenAI.api_key

# Chemin vers le fichier à téléverser
file_path = '4.jpg'  # Remplacez par le chemin réel
purpose = 'vision'  # Définir le but du fichier
image_id = None

# Fonction pour téléverser un fichier et récupérer l'ID
def upload_file(file_path, purpose):
    global image_id
    response = requests.post(
        'https://api.openai.com/v1/files',
        headers={
            'Authorization': f'Bearer {api_key}'
        },
        files={
            'file': open(file_path, 'rb')
        },
        data={
            'purpose': purpose
        }
    )
    if response.status_code == 200:
        print("Fichier téléversé avec succès.")
        response_data = response.json()
        print("Réponse:", response_data)
        # Récupérer l'ID du fichier téléversé
        image_id = response_data['id']
        print(f"Image ID: {image_id}")
    else:
        print("Erreur lors du téléversement du fichier.")
        print("Réponse:", response.json())

# Appeler la fonction de téléversement
upload_file(file_path, purpose)

# Afficher l'ID stocké
print(f"L'ID de l'image est: {image_id}")


# Code existant du script
client = OpenAI()
my_assistant = client.beta.assistants.retrieve("asst_grqTUmZsTeyGbV2iFpxoFWYP")
my_thread = client.beta.threads.create()

mood = "happy"
langue = "french"
hashtags = 4

my_thread_message = client.beta.threads.messages.create(
  thread_id=my_thread.id,
  role="user",
  content=[
    {"type": "text", 
     "text": f"{mood},{langue},{hashtags}"
    },
    {
        "type": "image_file",
        "image_file": {
            "file_id": f"{image_id}"
        }
    },
  ],
)

my_run = client.beta.threads.runs.create(
  thread_id=my_thread.id,
  assistant_id=my_assistant.id
)

while True:
    my_run = client.beta.threads.runs.retrieve(
        thread_id=my_thread.id,
        run_id=my_run.id
    )

    if my_run.status == "completed":
        print("\n")

        # Step 6: Retrieve the Messages added by the Assistant to the Thread
        all_messages = client.beta.threads.messages.list(
            thread_id=my_thread.id
        )

        print(f"User: {my_thread_message.content[0].text.value}")
        print(f"Assistant: {all_messages.data[0].content[0].text.value}")

        break
    elif my_run.status in ["queued", "in_progress"]:
        time.sleep(1)
        continue
    else:
        print(f"Run status: {my_run.status}")
        break

client.files.delete(f"{image_id}")