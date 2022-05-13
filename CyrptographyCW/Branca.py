
#To install branca run pip install pybranca

import json
import secrets
from branca import Branca

key = secrets.token_bytes(32)
branca = Branca(key)

string = json.dumps({
    "user" : "someone@example.com",
    "scope" : ["read", "write", "delete"]
})

token = branca.encode(string)
payload = branca.decode(token)

print(token)
print(payload)
          