import falcon
from .resources import *
from falcon_autocrud.middleware import Middleware

api = application = falcon.API(
    middleware=[Middleware()]
)

engine = create_engine('sqlite:///database.db')

api.add_route('/history', HistoryCollectionResource(engine))
