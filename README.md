# File Daemon 

HTTP API that provides following operations with files:
* upload file 
* download file
* delete file

> You may change config of service as you want (config/app_cgf.yaml). 
> Default config: 
>           HOST:   localhost
>           PORT:   8080

## Quick start 

1. Install required modules 

```bash 
pip3 install -r requirements.txt 
```
2. Run app.py 

3. Use swagger to test API

```
http://localhost:8080/api/doc
```
> For quick tests you may use presaved file - tests/test_files/dog.jpg 
> and hash - a91e56e5b56f92e3d0ceb62532b3f99c

> If you don't like swagger, you may use httpie 

## HTTPie Usage

* Upload file 

```bash
http -f POST http://localhost:8080/files cv@tests/test_files/dog.jpg 
```
* Download file 

```bash
http http://localhost:8080/files file==a91e56e5b56f92e3d0ceb62532b3f99c
```
* Delete file 

```bash
http DELETE http://localhost:8080/files file==a91e56e5b56f92e3d0ceb62532b3f99c
```

## Tests running 

* To increase verbosity 

```bash 
pytest -s tests
```

* To decrease verbosity 

```bash
pytest tests
```

OR

```bash
pytest -v tests
```
