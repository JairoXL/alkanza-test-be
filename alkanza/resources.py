from falcon_autocrud.resource import CollectionResource, SingleResource
from .models import *

# import json
# import falcon
# import dataset


class HistoryCollectionResource(CollectionResource):
    model = History
    methods = ['GET', 'POST']


# class NoteResource(SingleResource):
#     model = Note

# class Resource(object):
#     # def __init__(self, db_manager):
#     #     self.db = db_manager
#
#     def on_get(self, req, resp):
#         # history = []
#         # history = db['history'].all()
#         # doc = {
#         #     'images': [
#         #         {
#         #             'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
#         #         }
#         #     ]
#         # }
#
#         # Create a JSON representation of the resource
#         # resp.body = json.dumps(history, ensure_ascii=False)
#         resp.body = history
#
#         # The following line can be omitted because 200 is the default
#         # status returned by the framework, but it is included here to
#         # illustrate how this may be overridden as needed.
#         resp.status = falcon.HTTP_200