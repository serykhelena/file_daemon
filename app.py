from aiohttp import web
from aiohttp_swagger import *

import yaml

from api.routes import setup_routes


if __name__ == '__main__':
    app = web.Application()
    setup_routes(app)
    setup_swagger(app)

    with open('config/app_cfg.yaml') as cfg:
        data = yaml.safe_load(cfg)
        web.run_app(app, host=data['HOST'], port=data['PORT'])