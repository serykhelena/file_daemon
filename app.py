from aiohttp import web
from aiohttp_swagger import *

import yaml

from routes import setup_routes

app = web.Application()
setup_routes(app)

setup_swagger(app)


if __name__ == '__main__':
    
    
    with open('config/app_cfg.yaml') as cfg:
        data = yaml.safe_load(cfg)
        web.run_app(app, host=data['HOST'], port=data['PORT'])