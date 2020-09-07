from aiohttp import web
import json 

from routes import setup_routes


app = web.Application()
setup_routes(app)


if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)