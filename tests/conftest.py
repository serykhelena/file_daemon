import logging
import os

from aiohttp import web
import pytest 


from api.routes import setup_routes


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def create_app(loop):
    app = web.Application(loop=loop)
    logger.debug(f"App is created")
    setup_routes(app)
    logger.debug(f"Routes are created")
    return app

@pytest.fixture
async def client(aiohttp_client):
    client = await aiohttp_client(create_app)
    logger.debug(f"Client is created")
    return client



# @pytest.fixture(scope='session')
# def temp_file():
#     p = tmpdir.mkdir("sub").join("hello.txt")
#     p.write("Hello volks!")
