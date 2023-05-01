from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

in_memory_datastore = []

@app.route('/notes', methods=['PATCH', 'POST'])
@cross_origin()
def programming_languages_route():
   if request.method == 'POST':
       return list_notes(request.get_json(force=True))
   elif request.method == "PATCH":
       return create_note(request.get_json(force=True))

def list_notes(req):
   if 'url' in req:
      return [x for x in in_memory_datastore if x['url']==req['url']]

   return in_memory_datastore

def create_note(new_note):
   in_memory_datastore.append(new_note)
   return new_note


