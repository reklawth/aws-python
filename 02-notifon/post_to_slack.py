# coding: utf-8
import requests
url = '' # Replace with slack webhook URL
data = { "text": "Hello, world, and you too!" }
requests.post(url, json=data)
