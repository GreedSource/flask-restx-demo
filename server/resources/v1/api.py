from flask_restx import Resource, Namespace

api_resource = Namespace("api", "Api Resource")


@api_resource.route("/ping")
class Ping(Resource):
    def get(self):
        return {"message": "pong!"}
