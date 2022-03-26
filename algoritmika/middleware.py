import base64
import json
import re

import falcon

from algoritmika.models import user
from algoritmika.conf import config


class JSONTranslator:

    def process_response(self, req, resp, resource, req_succeeded):
        resp.set_header('Content-Type', 'application/json')
        resp.body = json.dumps(resp.body)


class BasicAuthMiddleware:
    basic_token = "bG9naW46cGFzc3dvcmQ="

    def check_excluded_rules(self, method, path):
        for method_rule, path_rule in config:
            path_rule = path_rule.replace('*', '.+') + "[/]?$"
            if method == method_rule and re.match(path_rule.replace('*', '.+'), path):
                break
        else:
            return False
        return True

    def process_resource(self, req, resp, resource, params):
        method = req.method
        path = req.path
        if not self.check_excluded_rules(method=method, path=path):
            auth_header = req.get_header("Authorization")
            if not auth_header:
                raise falcon.HTTPUnauthorized()
            _, access_token = auth_header.split(' ')
            if access_token != self.basic_token:
                raise falcon.HTTPUnauthorized()
        resp.context['user'] = user


class JWTAuthMiddleware:

    def process_resource(self, req, resp, resource, params):
        data = req.get_header("Authorization").split(' ')
        auth = str(user.login) + ":" + str(user.password)
        credentials = base64.b64encode(auth.encode('utf-8')).decode('utf-8')
        if data[1] != credentials:
            raise falcon.HTTPUnauthorized()
