

# DEFAULT_METHODS = ('GET', 'POST', 'PUT', 'DELETE')

# class RestEndpoint:
#     def __init__(self):
#         pass 

#     async def get(self):
#         pass 



async def handle(request):
    response_obj = { 'status' : 'success' }
    return web.Response(text=json.dumps(response_obj))