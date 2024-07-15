from googletrans import Translator

# Initialize the Translator
translator = Translator()

# Define the text to be translated
text = "Hello, how are you?"

# Translate the text
translated = translator.translate(text, src='en', dest='ta')

# Print the original and translated text
print(f"Original: {text}")
print(f"Translated: {translated.text}")
