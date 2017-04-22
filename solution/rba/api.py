from flask.views import MethodView
from flask import jsonify, request, abort

class rbaApi(MethodView):
    data = [
        {"id": 1, "name": u"Rob"},
        {"id": 2, "name": u"Jim"},
        {"id": 3, "name": u"Rambo"}
        ]
        
    def get(self):
        return jsonify({"data": self.data})