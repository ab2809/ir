import requests
import pyperclip

url = "https://raw.githubusercontent.com/98987777/iot/refs/heads/main/list.py"
response = requests.get(url)
pyperclip.copy(response.text)
