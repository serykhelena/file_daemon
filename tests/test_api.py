import logging

import pytest

from tools.files import save_file

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def test_delete(client): 
    resp = await client.delete("/files?file=a91e56e5b56f92e3d0ceb62532b3f99c")

    # save back file not to break other tests 
    with open('tests/test_files/dog.jpg','rb') as file_:
        save_file('a9/', 'a91e56e5b56f92e3d0ceb62532b3f99c', file_.read())

    assert resp.status == 200 

async def test_bad_delete(client):
    resp = await client.delete("/files?file=a")

    assert resp.status == 400
    assert resp.content_type == 'text/plain'


async def test_upload(client):
    files = {'file': open('tests/test_files/dog.jpg','rb')}
    resp = await client.post("/files", data=files)

    assert resp.status == 200 
    assert resp.content_type == 'text/plain'


async def test_download(client): 
    resp = await client.get("/files?file=a91e56e5b56f92e3d0ceb62532b3f99c")

    assert resp.status == 200
    assert resp.content_type == 'application/octet-stream'


async def test_bad_download(client):
    resp = await client.get("/files?file=a")

    assert resp.status == 400 
    assert resp.content_type == 'text/plain'


