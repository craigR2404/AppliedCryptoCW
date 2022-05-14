import jwt 
SECRET_KEY = "python_jwt"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZW5kZXIiOiJFZGluYnVyZ2ggTmFwaWVyIFlvIiwibWVzc2FnZSI6IkpXVHMgYXJlIHRoZSBiYWluIG9mIGFsbCBkZXZlbG9wZXJzIGxpdmVzISIsImRhdGUiOiIyMDIyLTA1LTE0IDE4OjQ0OjUzLjkwNTk1NyJ9.0HKlc-HC5smKT2WVFFv24Q19Y9xcfKLQFDKWQ3cDsxE"
try:
    decode_data = jwt.decode(jwt=token, \
                            key=SECRET_KEY, algorithms="HS256")
    print(decode_data)
except Exception as e:
    message = f"Token is invalid --> {e}"
    print({"message": message})