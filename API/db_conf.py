import aiomysql
import asyncio
import uvloop
import requests
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
def koneksi():
    loop = asyncio.get_event_loop()
    conn = aiomysql.connect(host='127.0.0.1',port=3306,user='root',password='',db='bajigur',loop=loop)
    return conn
