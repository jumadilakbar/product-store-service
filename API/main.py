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
import db_conf
import datetime
import jwt
import uuid
from sanic_jwt_extended.tokens import Token
# QUery 
from query.product import bp as product

app = Sanic("Project_Tees")
app.blueprint(swagger_blueprint)
@app.route("/")
async def test(request):
  return json({"hello": "Monggo Cek Swaggernya"})

CORS(app,automatic_options=True)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=720)
JWTManager(app)
class Login :
    email = str
    password = str
@app.route('/login', methods=['POST'])
@doc.consumes(Login, location="body")
async def login(request):
    body = request.json
    email = body.get('email')
    password = body.get('password')
    core = await db_conf.koneksi()
    async with core.cursor() as cur:
        await cur.execute('SELECT user_id, role_id, email, username from user WHERE email= %s and password= %s',(email,password))
        rest = await cur.fetchall()
    if len(rest)>0:
        data =  []
        for i in rest:
            data.append({
                "email":email, 
                "user_id":i[0],
                "role_id":i[1],
                "username":i[3]
            })
        access_token = await create_access_token(identity=data, app=request.app)
        refresh_token = await create_refresh_token(identity=str(uuid.uuid4()) , app=request.app)
        return json(dict(access_token=access_token,
                        refresh_token=refresh_token,
                        status="status success",
                        Authorization= "Bearer"
                        ), status=200)
    else:
        return json({"msg": "Bad username or password"}, status=403)
@app.route('/who_me', methods=['GET'])
@jwt_required
async def who_me(request: Request, token: Token):
    # print(str(token))
    current_user = token.jwt_identity
    for i in current_user:
        print(i['email'])
    # print(current_user["email"])
    print(type(current_user))
    return json(dict(
        status='status_success',
        logined_as=current_user
    )) 
app.blueprint(product)

app.config.API_VERSION = '1.0.0'
app.config.API_TITLE = 'Service Product Bajigur'
app.config.API_TERMS_OF_SERVICE = 'Use with caution!'
app.config.API_CONTACT_EMAIL = 'muhamadjumadilakbar@gmail.com'

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000,debug=True)