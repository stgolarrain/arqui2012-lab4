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
            self.response.write('status 404')
    
    def post(self):
        if self.request.headers['Content-Type']=='application/json':
            data = json.load(open("datos.json", "r"))
            self.response.write('Agregando texto como objeto de Json\n')
            data_input = self.request.body_file
            nline = 0
            for line in data_input:
                nline += 1
            data_input = self.request.body_file
            i = 0
            data2 = ''
            for line in data_input:
                if i  > 1 & i != nline:
                    data2 += line
            self.response.write(data2)
            self.response.write(self.request.body)
            data['mensajes'].append(data2)
            archivo = open("datos.json", "w")
            archivo.write(json.dumps(data))
            archivo.close()
        else:
            self.response.write('Agregando texto plano')
            data = json.load(open("datos.json", "r"))
            self.response.write('Agregando texto como objeto de Json')
            data['mensajes'].append(self.request.params['mensaje'])
            archivo = open("datos.json", "w")
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
    