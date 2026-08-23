from linkedin_api import Linkedin
import os

from flask import Flask
from flask import request

from flask_cors import CORS


app = Flask(__name__)
CORS(app)

from dotenv import load_dotenv
load_dotenv()
print("loaded env")

# Authenticate using any Linkedin user account credentials
api = Linkedin('ping.mithil@gmail.com', os.environ['LINKEDIN_PWD'])
print("authenticated")

@app.post("/api/send-linkedin-connection")
def main():
    print(request.args)
    

    # GET a profile
    people = api.search_people(request.args['query'])
    print("people", people)
    if len(people) > 0:
        person = people[0]
        print(person)

        result = api.add_connection(person['urn_id'], message=request.args['message'])
        return {'success': not result}
    else:
        return {'success': False}


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)