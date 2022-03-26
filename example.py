from wsgiref.simple_server import make_server

import falcon
from classic.aspects import points
from classic.http_api import App
from classic.sql_storage import TransactionContext
from sqlalchemy import create_engine

from adapters import DBSettings, metadata
from adapters import repo
from adapters.controllers import Departments, Employees
from algoritmika.exception import NotStatusExceptioms
from algoritmika.middleware import JSONTranslator
from algoritmika.views import (
    UserController, UsersController,
    BookBaseViews, NoteListCreateView, NoteRetrieveView,
    IssueRetrieveView, IssueListCreateView, SortedIssue,
    TackNumberFour, FilterBaseView, AuthLogin
)
from aplications.dataclases import Chat, Department, Employee
from aplications.service import ServiceDepartment, ServiceEmployee

db_settings = DBSettings(DB_URL="sqlite:///hello.db")

engine = create_engine(db_settings.DB_URL, echo=True)
metadata.create_all(engine)

transaction_ctx = TransactionContext(bind=engine, expire_on_commit=False)


repo_order = repo.Proba(context=transaction_ctx)
repo_employee = repo.SQLiteRepository(model=Department, context=transaction_ctx)
employee_repositories = repo.EmployeeRepository(model=Employee, context=transaction_ctx)

service_department = ServiceDepartment(repo_employee=repo_employee)
service_employee = ServiceEmployee(employee_repositories=employee_repositories)

department = Departments(service_department=service_department)
employee = Employees(service_employee=service_employee)


class ThingsResource:
    @points.join_point
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        chat = Chat(pk=6, order_date='@@@@@@@@@@@@@@')
        c = repo_order.add(chat)
        resp.body = c


points.join(transaction_ctx)


middleware = [
    JSONTranslator(),
    # BasicAuthMiddleware(),

]
app = App(middleware=middleware)
app.add_error_handler(NotStatusExceptioms)

# Resources are represented by long-lived class instances
things = ThingsResource()
user_controller = UserController()
users_controller = UsersController()
books_controller = BookBaseViews()


# things will handle all requests to the '/things' URL path
app.add_route('/things', things)
app.add_route('/department/', department)
app.add_route('/employee/', employee)
app.add_route('/users/', users_controller)
app.add_route('/users/{user_id}', user_controller)
app.add_route('/books/{book_id}', books_controller)
app.add_route('/notes/{entity_id}', NoteRetrieveView())
app.add_route('/notes/', NoteListCreateView())
app.add_route('/issues/', IssueListCreateView())
app.add_route('/issues/{entity_id}', IssueRetrieveView())
app.add_route('/sorted-issues/', SortedIssue())
app.add_route('/status/{status}', TackNumberFour())
app.add_route('/filters/', FilterBaseView())
app.add_route('/login/', AuthLogin())

if __name__ == '__main__':
    with make_server(host="127.0.0.1", port=8003, app=app) as httpd:
        httpd.serve_forever()
