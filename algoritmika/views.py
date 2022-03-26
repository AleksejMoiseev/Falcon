import falcon
from falcon_jinja2 import FalconTemplate

from adapters.repo import Proba
from algoritmika.constans import Book, book, books, note, issue, STATUS
import json
import base64
from algoritmika.models import user

from algoritmika.exception import NotStatusExceptioms
from algoritmika.utils import sorted_entities, get_params_filter, ORM_FALCON
from aplications.dataclases import Chat

falcon_template = FalconTemplate()


# class ThingsResource:
#     @falcon_template.render(template='index.html')
#     def on_get(self, req, resp):
#         """Handles GET requests"""
#         resp.status = falcon.HTTP_200
#         resp.content_type = falcon.MEDIA_TEXT
#         chat = Chat(order_date='Hello')
#         c = repo.add(chat)
#         resp.body = c
#         resp.context = {'content': resp.text, 'title': "HELLO"}


class UserController:
    def on_get(self, req, resp, user_id):
        if int(user_id) == 1:
            resp.text = 'Крутяк'
            resp.status = falcon.HTTP_200
            resp.context = {'content': resp.text, 'title': "USERS"}
        else:
            raise falcon.HTTPNotImplemented('Полная задница')

    def on_post(self, req, resp, user_id):
        pass

    def on_put(self, req, resp, user_id):
        pass

    def on_patch(self, req, resp, user_id):
        pass


class UsersController:
    def on_get(self, req, resp, user_id):
        pass

    def on_post(self, req, resp, user_id):
        pass


class BookBaseViews:

    def on_get(self, req, resp, book_id):
        for b in books:
            if b['id'] == int(book_id):
                resp.body = json.dumps(b)
                resp.status = falcon.HTTP_200
            else:
                raise falcon.HTTPNotImplemented('Полная задница')


class BaseView:
    entity = None


class ListCreateBaseView(BaseView):

    def on_get(self, req, resp):
        limit = req.get_param_as_int('limit') or 0
        offset = req.get_param_as_int('offset') or len(self.entity)
        resp.body = self.entity[limit:offset]
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        params: dict = req.get_media()
        keys = self.entity[0].keys()
        entity = dict([(k, '') for k in keys])
        for k in params:
            entity[k] = params[k]
        self.entity.append(entity)
        resp.body = json.dumps(entity)
        resp.status = falcon.HTTP_200


class RetrieveBaseView(BaseView):

    def on_get(self, req, resp, entity_id):
        for n in self.entity:
            if n['id'] == int(entity_id):
                resp.body = json.dumps(n)
                resp.status = falcon.HTTP_200

    def on_put(self, req, resp, entity_id):
        params: dict = req.context
        for n in note:
            if n['id'] == int(entity_id):
                for key in params:
                    n[key] = params[key]
                    resp.body = json.dumps(n)
                    resp.status = falcon.HTTP_200

    def on_patch(self, req, resp, entity_id):
        params: dict = req.context
        for n in self.entity:
            if n['id'] == int(entity_id):
                for key in params:
                    n[key] = params[key]
                    resp.body = json.dumps(n)
                    resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, entity_id):
        for idx, entity in enumerate(self.entity):
            if entity['id'] == entity_id:
                resp.body = json.dumps(self.entity.pop(idx))
                resp.status = falcon.HTTP_205


class NoteListCreateView(ListCreateBaseView):
    entity = note


class NoteRetrieveView(RetrieveBaseView):
    entity = note


class IssueListCreateView(ListCreateBaseView):
    entity = issue


class IssueRetrieveView(RetrieveBaseView):
    entity = issue


class SortedIssue(IssueListCreateView):
    def on_get(self, req, resp):
        sort_by = req.get_param('sort_by')
        order_by = req.get_param('order_by')
        entities = sorted_entities(list_of_entity=self.entity, key=sort_by, parameter=order_by)
        resp.body = json.dumps(entities)
        resp.status = falcon.HTTP_200


class TackNumberFour(BaseView):
    entity = note

    def on_get(self, req, resp, status):
        status = STATUS.get(status)
        if not status:
            raise NotStatusExceptioms()
        tmp = []
        for entity in self.entity:
            if entity['status'] == status:
                tmp.append(entity)
        resp.body = tmp
        resp.status = falcon.HTTP_200


class FilterBaseView(BaseView):
    entity = note

    def on_get(self, req, resp):
        keys = self.entity[0].keys()
        if not keys:
            raise falcon.HTTPInvalidParam(msg="Entity d`nt have entity", param_name='note')
        params: dict = req.params
        tmp_list_entity = self.entity.copy()
        for key in keys:
            if not params.get(key):
                continue
            func, parameters = get_params_filter(key=key, params=params)
            tmp_list_entity = ORM_FALCON[func](tmp_list_entity, **parameters)
        resp.body = tmp_list_entity
        resp.status = falcon.HTTP_200


class AuthLogin:

    def on_post(self, req, resp):
        login = 'login:password'.encode('utf-8')
        token = base64.b64encode(login)
        user.token = token
        resp.body = token.decode('utf-8')

    def on_get(self, req, resp):
        login = 'password'.encode('utf-8')
        token = base64.b64encode(login)
        user.token = token
        resp.body = token.decode('utf-8')
