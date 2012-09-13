import webapp2
import json
import sys

from warnings import catch_warnings


class HelloWebapp2(webapp2.RequestHandler):
#class Hello:
    def get(self):
        try:
            archivo = open("datos.json",'r')
            data = json.load(archivo)
            archivo.close()
            self.response.write(json.dumps(data))
            self.response.headers['Content-Type']='application/json'
        except IOError as e:
            self.response.set_status(404)
    
    def post(self):
        try:
            data = json.load(open("datos.json", "r"))
        except Exception:
            data = '{"mensajes" : []}'
        if self.request.headers['Content-Type']=='application/json':
            input = self.request.body
            self.response.write('JSON Object')
            #input = json.loads(input)
        else:
            input = self.request.POST['mensaje']
            self.response.write('Texto plano')
        data['mensajes'].append(input)
        archivo = open('datos.json', 'w')
        archivo.write(json.dumps(data))
        archivo.close()
        

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='8080')

if __name__ == '__main__':
    main()
    #hello = Hello()
    