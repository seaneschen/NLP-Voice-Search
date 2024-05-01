'''
Manages the input and validation of the OpenAI API key
'''
import os
from cryptography.fernet import Fernet
class APIKeyManager:
    def __init__(self):
        self.key_file = 'api_key.key'
        # Generate a Fernet key if it doesn't exist and set it as an environment variable
        self.fernet_key = os.environ.get('FERNET_KEY') or self.generate_fernet_key()
        self.fernet = Fernet(self.fernet_key)
    def generate_fernet_key(self):
        key = Fernet.generate_key()
        os.environ['FERNET_KEY'] = key.decode()  # Save the key as a string in the environment variable
        return key
    def input_key(self, key):
        encrypted_key = self.fernet.encrypt(key.encode())
        with open(self.key_file, 'wb') as file:
            file.write(encrypted_key)
    def validate_key(self, key):
        # Placeholder for actual API key validation logic
        # In a real-world scenario, you would hit an endpoint that validates the key
        # For this example, we assume that if the key is not empty, it is valid
        return key is not None and key != ""
    def get_key(self):
        try:
            with open(self.key_file, 'rb') as file:
                encrypted_key = file.read()
            decrypted_key = self.fernet.decrypt(encrypted_key).decode()
            return decrypted_key
        except FileNotFoundError:
            return None