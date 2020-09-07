from views import FileDaemon 


def setup_routes(app):
    daemon = FileDaemon()

    app.router.add_route('GET', '/files', daemon.get)
    app.router.add_route('POST', '/files', daemon.post)
    app.router.add_route('DELETE', '/files', daemon.delete)
    
