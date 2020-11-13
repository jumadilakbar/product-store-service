from sanic import Sanic
from sanic.response import json
from sanic.response import json
from sanic_openapi import swagger_blueprint
from sanic_cors import CORS, cross_origin
from sanic_openapi import doc
from sanic import Blueprint
# from sanic_openapi import doc
# from sanic.request import RequestParameters
# jwt_package
from sanic.response import json
from sanic.request import Request
from sanic_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    create_refresh_token)
# import jwt
# import db_conf
import datetime
import jwt
import uuid
from sanic_jwt_extended.tokens import Token
# QUery

app = Sanic("hello_example")
app.blueprint(swagger_blueprint)
@app.route("/")
async def test(request):
  return json({"hello": "world"})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000,debug=True)