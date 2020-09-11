import logging

from aiohttp import web

from daemon.hash import generate_hash, get_subfolder_name
from daemon.files import save_file, get_path_to_file, delete_file


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class FileDaemon:

    async def get(self, request):
        """
        ---
        description: This end-point allows to download files.
        tags:
        - Download file
        parameters:
        - in: query
          name: file
          type: string
          description: hash of file 
        produces:
        - application/octet-stream
        responses:
            "200":
                description: File with the name of specified hash 
            "400":
                description: Bad request
        """
        try:
            file_hash = request.query['file']
            logger.debug(f"Hash is found!")
        except KeyError as err:
            logger.error(f"No parameter 'file' in request query")
            return web.Response(text="Use parameter 'file' to specified file hash", status=400)
        
        try:
            resp = web.FileResponse(
                get_path_to_file(file_hash),
                headers={
                    'content-disposition': 'attachment; filename="my_fname"'
                })
            return resp 
        except IOError as err:
            return web.Response(text=f"File {file_hash} doesn't exist!", status=400)
    

    async def post(self, request):
        """
        ---
        description: This end-point allows to upload new file.
        tags:
        - Upload file
        consumes:
        - multipart/form-data
        parameters:
        - in: formData
          name: upfile
          type: file
          description: The file to upload.
        produces:
        - text/plain
        responses:
            "200":
                description: successful operation. Return hash 
            "400":
                description: Bad request
        """
        try:
            reader = await request.multipart()
            client_file = await reader.next()
            file_data = await client_file.read(decode=True)
        except (AssertionError, AttributeError):
            return web.Response(text='Uploading file is not found!', status=400)

        file_name = client_file.filename

        hash_ = generate_hash(file_data)
        save_file(get_subfolder_name(hash_), hash_, file_data)

        return web.Response(text=hash_, status=200)
    

    async def delete(self, request):
        """
        ---
        description: This end-point allow to delete file.
        tags:
        - Delete file
        parameters:
        - in: query
          name: file
          type: string
          description: hash of file 
        produces:
        - text/plain
        responses:
            "200":
                description: successful operation
            "400":
                description: Bad request
        """
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
