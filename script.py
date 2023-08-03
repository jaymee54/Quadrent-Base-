# from flask import Flask, jsonify, render_template
# from flask_cors import CORS
#
# app = Flask(__name__)
# CORS(app)
#
# titles = ['Title 1', 'Title 2']
# title_index = 0
#
# @app.route('/')
# def index():
#     return render_template('quadrentbase.html')
#
# @app.route('/api/title', methods=['GET'])
# def get_title():
#     global title_index
#     title = titles[title_index]
#     title_index = (title_index + 1) % len(titles)
#     return jsonify({'title': title})
#
# if __name__ == '__main__':
#     app.run()
#
# from http.server import BaseHTTPRequestHandler, HTTPServer
# import json
#
# data = {
#     'title': 'Title 1',
#     'number': 42,
#     'text_path': 'Support files/MyText.txt',
#     'image_path': 'Support files/tricentis-tosca-logo-images.png'
# }
#
# class RequestHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == '/api/data':
#             self.send_response(200)
#             self.send_header('Content-type', 'application/json')
#             self.end_headers()
#             self.wfile.write(json.dumps(data).encode())
#         else:
#             self.send_response(404)
#             self.end_headers()
#             self.wfile.write(b'Not found')
#
# def run():
#     server_address = ('', 8000)
#     httpd = HTTPServer(server_address, RequestHandler)
#     print('Server running on http://localhost:8000')
#     httpd.serve_forever()
#
# if __name__ == '__main__':
#     run()

from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

data = {
    'title': 'Title 1',
    'number': 42,
    'text_path': 'Support files/MyText.txt',
    'image_path': 'Support files/tricentis-tosca-logo-images.png'
}

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def do_GET(self):
        if self.path == '/api/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not found')

def run():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, CORSRequestHandler)
    print('Server running on http://localhost:8080')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
