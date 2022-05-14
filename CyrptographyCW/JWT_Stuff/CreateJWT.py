import datetime
import jwt # import jwt library
SECRET_KEY = "python_jwt"
# json data to encode
json_data = {
    "sender": "Edinburgh Napier Yo",
    "message": "JWTs are the bain of all developers lives!",
    "date": str(datetime.datetime.now())
}
# encode the data with SECRET_KEY and 
# algorithm "HS256" -> Symmetric Algorithm
encode_data = jwt.encode(payload=json_data, \
                        key=SECRET_KEY, algorithm="HS256")
print(encode_data) # print the encoded token