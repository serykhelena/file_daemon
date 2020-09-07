import logging

from aiohttp import web

from tools.hash import generate_hash, get_subfolder_name
from tools.files import save_file

routes = web.RouteTableDef()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@routes.post('/upload')
async def upload(request):
    try:
        reader = await request.multipart()
    except AssertionError as err:
        return web.Response(text='Uploading file is not found!')

    client_file = await reader.next()
    file_data = await client_file.read(decode=True)

    file_name = client_file.filename
    file_extension = file_name[file_name.rfind('.'):]

    hash_ = generate_hash(file_data)
    save_file(get_subfolder_name(hash_), hash_ + file_extension, file_data)

    data = {
        'hash': hash_
    }
    return web.json_response(data)


@routes.get('/download')
async def download(request):
    return web.Response(text='Download file')


@routes.delete('/delete')
async def delete(request):
    return web.Response(status=200, text='Delete file')

