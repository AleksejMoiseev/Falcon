import json
import falcon


class NotStatusExceptioms(Exception):
    @staticmethod
    def handle(req, resp, exc, params):
        msg = f"NOT STATUS  = {params['status']}"
        resp.set_header("X-Custom-Header", "*")
        resp.body = json.dumps(msg)
        resp.status = falcon.HTTP_404


class BadRequest(Exception):
    @staticmethod
    def handle(req, resp, exc, params):
        resp.set_header("X-Custom-Header", "*")
        resp.body = f"Parameters in a request cannot be validated"
        resp.status = falcon.HTTP_404
