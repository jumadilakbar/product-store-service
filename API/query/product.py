
from sanic.response import json
from sanic import Blueprint
from sanic_openapi import doc
from sanic.request import RequestParameters
from sanic.exceptions import ServerError
import db_conf
import datetime 
# JWT Package
from sanic.request import Request
from sanic_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    create_refresh_token)
import uuid
from sanic_jwt_extended.tokens import Token

class Pagination:
    page_size = int
    page_num = int

class Usersesion:
    user_id = int

bp = Blueprint('blueprint_product')

@bp.get('/product/all')
@doc.summary("get all data from  product list")
@doc.tag('Product')
async def all_product(request):
    core = await db_conf.koneksi()
    async with core.cursor() as cur:
        # status = 'Active'
        sql = 'select * from tb_product_list'
        await cur.execute(sql)
        row_headers=[x[0] for x in cur.description]
        rest = await cur.fetchall()            
    data=[]
    for result in rest:
        data.append(dict(zip(row_headers,result)))

    status = "success get data"
    return json({
            "status":status,
            "data":data,
            "message":"get all data master departement with pagination"
            })
    # return json({"hello": "world"})


@bp.post('/product/show_data')
@doc.summary("get all data product pagination")
@doc.tag('Product')
@doc.consumes(Pagination, location="body")
# @jwt_required
async def product_page(request):
    try:
        body = request.json
        page_size = body.get('page_size')
        page_num = body.get('page_num')
        index = page_size * (page_num - 1)
        core = await db_conf.koneksi()
        async with core.cursor() as cur:
            await cur.execute("SELECT tpl.product_id , tpl.product_name, tpl.price, tk.kategori_name, tpl.id_color, tpl.rating from tb_product_list tpl, tb_kategori tk where tpl.id_kategori = tk.kategori_id limit  %s, %s",(index,page_size))
            row_headers=[x[0] for x in cur.description]
            rest = await cur.fetchall()            
        data=[]
        for result in rest:
            x =list(result)
            x[4]= x[4].split(",")
            result = tuple(x)
            data.append(dict(zip(row_headers,result)))

        async with core.cursor() as cur:
            await cur.execute('select count(*) from tb_product_list')
            total = await cur.fetchall()
        
        status = "success get data"
        return json({
            "status":status,
            "data":data,
            "total":total[0][0],
            "message":"get all data product with pagination"
            })
    except:
        return json({
            "status":"failed request",
            "data":"someting wrong",
            "message":"erorr"
            })

@bp.get('/product/tranding')
@doc.summary("get all data product tranding")
@doc.tag('Product')
# @doc.consumes(Pagination, location="body")
async def product_tranding(request):
    try:
        body = request.json
        
        core = await db_conf.koneksi()
        async with core.cursor() as cur:
            sql_rlt = """
            SELECT tpl.product_id , tpl.product_name, tpl.price, tk.kategori_name, tpl.id_color, tpl.rating 
            from tb_product_list tpl, tb_kategori tk, tb_tranding_product ttp 
            where tpl.id_kategori = tk.kategori_id and ttp.id_prduct =tpl.product_id
            """
            await cur.execute(sql_rlt)
            row_headers=[x[0] for x in cur.description]
            rest = await cur.fetchall()            
        data=[]
        for result in rest:
            x =list(result)
            x[4]= x[4].split(",")
            result = tuple(x)
            data.append(dict(zip(row_headers,result)))

        async with core.cursor() as cur:
            await cur.execute('select count(*) from tb_product_list')
            total = await cur.fetchall()
        
        status = "success get data"
        return json({
            "status":status,
            "data":data,
            "total":total[0][0],
            "message":"get all data product with pagination"
            })
    except:
        return json({
            "status":"failed request",
            "data":"someting wrong",
            "message":"erorr"
            })

@bp.get('/product/history_user_order')
@doc.summary("get data recomendation history order user")
@doc.tag('Product')
# @doc.consumes({"user": {"departement_id":int}}, location="body")
@jwt_required
async def history_user_order(request, token=Token):
    try:
        body = request.json
        current_user = token.jwt_identity
        for i in current_user:
            # email = i['email']
            user_id = i['user_id']
            role_id = i['role_id']
            # username = i['username']
        print(role_id,user_id)
        core = await db_conf.koneksi()
        async with core.cursor() as cur:
            sql ="""
            SELECT * from role r, user b 
            WHERE r.role_id=b.role_id and r.role_id=%s and b.user_id=%s 
            """
            await cur.execute(sql,(role_id,user_id))
            cek_role = await cur.fetchall()
        
        if len(cek_role)>0:
            # departement_id = body.get('departement_id')
            async with core.cursor() as cur:
                sql_detail = """
                SELECT tpl.product_id , tpl.product_name, tpl.price, tk.kategori_name, tpl.id_color, tpl.rating 
                from tb_product_list tpl, tb_kategori tk, tb_rekomendation_order trh 
                where tpl.id_kategori = tk.kategori_id 
                and trh.product_id =tpl.product_id and trh.user_id =%s
                """
                await cur.execute(sql_detail,(user_id))
                row_headers=[x[0] for x in cur.description]
                rest = await cur.fetchall()            
            data=[]
            for result in rest:
                x =list(result)
                x[4]= x[4].split(",")
                result = tuple(x)
                data.append(dict(zip(row_headers,result)))

            status = "success get data"
        else:
            data = "user invalid"
            status = "not success get data"
        return json({
            "status":status,
            "data":data,
            "message":"get all data product by history order user"
            })
    except:
        return json({
            "status":"failed request",
            "data":"someting wrong",
            "message":"erorr"
            })

@bp.get('/product/history_user_search')
@doc.summary("get data recomendation history search product user")
@doc.tag('Product')
# @doc.consumes({"user": {"departement_id":int}}, location="body")
@jwt_required
async def history_user_search(request, token=Token):
    try:
        body = request.json
        current_user = token.jwt_identity
        for i in current_user:
            # email = i['email']
            user_id = i['user_id']
            role_id = i['role_id']
            # username = i['username']
        print(role_id,user_id)
        core = await db_conf.koneksi()
        async with core.cursor() as cur:
            sql ="""
            SELECT * from role r, user b 
            WHERE r.role_id=b.role_id and r.role_id=%s and b.user_id=%s 
            """
            await cur.execute(sql,(role_id,user_id))
            cek_role = await cur.fetchall()
        
        if len(cek_role)>0:
            # departement_id = body.get('departement_id')
            async with core.cursor() as cur:
                sql_detail = """
                SELECT tpl.product_id , tpl.product_name, tpl.price, tk.kategori_name, tpl.id_color, tpl.rating 
                from tb_product_list tpl, tb_kategori tk, tb_rekomendation_history trh 
                where tpl.id_kategori = tk.kategori_id 
                and trh.product_id =tpl.product_id and trh.user_id =%s
                """
                await cur.execute(sql_detail,(user_id))
                row_headers=[x[0] for x in cur.description]
                rest = await cur.fetchall()            
            data=[]
            for result in rest:
                x =list(result)
                x[4]= x[4].split(",")
                result = tuple(x)
                data.append(dict(zip(row_headers,result)))

            status = "success get data"
        else:
            data = "user invalid"
            status = "not success get data"
        return json({
            "status":status,
            "data":data,
            "message":"get all data product by history search product user"
            })
    except:
        return json({
            "status":"failed request",
            "data":"someting wrong",
            "message":"erorr"
            })

@bp.post('/product/asosiasi_data')
@doc.summary("get data recomendation berdasarkan asosiasi data")
@doc.tag('Product')
@doc.consumes({"user": {"product_id":int}}, location="body")
# @jwt_required
async def asosiasi_data(request):
    try:
        body = request.json 
        product_id = body.get('product_id')
        core = await db_conf.koneksi()

        async with core.cursor() as cur:
            sql_detail = """
            SELECT * from tb_asosiasi_product tap where tap.produk_id =%s
            """
            await cur.execute(sql_detail,(product_id))
            # row_headers=[x[0] for x in cur.description]
            rest = await cur.fetchall()            
        data=[]
        for result in rest:
            list_prd_id = result[1].split(",")
            print(list_prd_id)
            for i in list_prd_id:
                async with core.cursor() as cur:
                    sql_asosiasi = """
                    SELECT tpl.product_id , tpl.product_name, tpl.price, tk.kategori_name, tpl.id_color, tpl.rating 
                    from tb_product_list tpl, tb_kategori tk
                    where tpl.id_kategori = tk.kategori_id and tpl.product_id =%s
                    """
                    await cur.execute(sql_asosiasi,(i))
                    row_headers=[x[0] for x in cur.description]
                    rest1 = await cur.fetchall() 
                    for result1 in rest1:
                        x =list(result1)
                        x[4]= x[4].split(",")
                        result1 = tuple(x)
                        data.append(dict(zip(row_headers,result1)))
        # print(rest1)
        status = "success get data"
        return json({
            "status":status,
            "data":data,
            "message":"get all data asosiation product"
            })
    except:
        return json({
            "status":"failed request",
            "data":"someting wrong",
            "message":"erorr"
            })

@bp.post('/product/similarity')
@doc.summary("get data recomendation berdasarkan kemiripan data")
@doc.tag('Product')
@doc.consumes({"user": {"product_id":int}}, location="body")
# @jwt_required
async def similarity(request):
    try:
        body = request.json 
        product_id = body.get('product_id')
        core = await db_conf.koneksi()

        async with core.cursor() as cur:
            sql_detail = """
            SELECT * from tb_recomendasi_similarity tap where tap.similar_product_id =%s
            """
            await cur.execute(sql_detail,(product_id))
            # row_headers=[x[0] for x in cur.description]
            rest = await cur.fetchall()            
        data=[]
        for result in rest:
            list_prd_id = result[1].split(",")
            print(list_prd_id)
            for i in list_prd_id:
                async with core.cursor() as cur:
                    sql_asosiasi = """
                    SELECT tpl.product_id , tpl.product_name, tpl.price, tk.kategori_name, tpl.id_color, tpl.rating 
                    from tb_product_list tpl, tb_kategori tk
                    where tpl.id_kategori = tk.kategori_id and tpl.product_id =%s
                    """
                    await cur.execute(sql_asosiasi,(i))
                    row_headers=[x[0] for x in cur.description]
                    rest1 = await cur.fetchall() 
                    for result1 in rest1:
                        x =list(result1)
                        x[4]= x[4].split(",")
                        result1 = tuple(x)
                        data.append(dict(zip(row_headers,result1)))
        # print(rest1)
        status = "success get data"
        return json({
            "status":status,
            "data":data,
            "message":"get all data asosiation product"
            })
    except:
        return json({
            "status":"failed request",
            "data":"someting wrong",
            "message":"erorr"
            })
