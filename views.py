import logging

from aiohttp import web

from tools.hash import generate_hash, get_subfolder_name
from tools.files import save_file, get_path_to_file, delete_file

routes = web.RouteTableDef()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@routes.post('/upload')
async def upload(request):
    try:
        reader = await request.multipart()
    except AssertionError as err:
        return web.Response(text='Uploading file is not found!', status=400)

    client_file = await reader.next()
    file_data = await client_file.read(decode=True)

    file_name = client_file.filename

    hash_ = generate_hash(file_data)
    save_file(get_subfolder_name(hash_), hash_, file_data)

    return web.Response(text=hash_, status=200)


@routes.get('/download')
async def download(request):
    try:
        file_hash = request.query['file']
    except KeyError as err:
        logger.error(f"No parameter 'file' in request query")
        return web.Response(text="Use parameter 'file' to specified file hash", status=400)
    
    try:
        return web.FileResponse(get_path_to_file(file_hash))
    except IOError as err:
        return web.Response(text=f"File {file_hash} doesn't exist!", status=400)


@routes.delete('/delete')
async def delete(request):
    try:
        file_hash = request.query['file']
    except KeyError as err:
        logger.error(f"No parameter 'file' in request query")
        return web.Response(text="Use parameter 'file' to specified file hash")
    
    try: 
        delete_file(file_hash)
        return web.Response(text=f"File {file_hash} was removed successfully!", status=200)
    except IOError as err:
        return web.Response(text=f"File {file_hash} doesn't exist!", status=400)

