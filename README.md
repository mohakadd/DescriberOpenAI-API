# Describer

Ce dépôt contient un script Python permettant d'utiliser l'API OpenAI pour analyser une image.
Le script téléverse un fichier image, exécute un assistant prédéfini et affiche la réponse obtenue.

## Prérequis

- Python 3.8 ou supérieur
- Les bibliothèques `requests` et `openai`

Installez les dépendances avec :

```bash
pip install -r requirements.txt
```

## Configuration

Définissez la variable d'environnement `OPENAI_API_KEY` contenant votre clé API OpenAI.
Vous pouvez la placer dans un fichier `.env` ou l'exporter directement dans votre shell.

## Utilisation

1. Modifiez la variable `file_path` dans `application.py` pour indiquer le chemin de l'image à décrire.
2. Si nécessaire, ajustez l'identifiant de l'assistant (`asst_grqTUmZsTeyGbV2iFpxoFWYP`).
3. Exécutez le script :

```bash
python application.py
```

Le programme procède alors au téléversement de l'image, lance l'assistant et affiche le résultat dans la console. Une fois terminé, le fichier téléversé est supprimé.


