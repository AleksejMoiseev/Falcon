from classic.aspects import points
from classic.components.component import component
from falcon import Request, Response

from aplications.interface import DepartmentServiceInterface, EmployeeServiceInterface
import falcon


@component
class Departments:
    service_department: DepartmentServiceInterface

    @points.join_point
    def on_post(self, req: Request, resp: Response):
        params = req.get_media()
        department = self.service_department.create_department(params)
        result = {
            'result': "success",
            'id': department.id,
            'name': department.name,
        }
        resp.body = result
        resp.status = falcon.HTTP_201


@component
class Employees:
    service_employee: EmployeeServiceInterface

    @points.join_point
    def on_post(self, req: Request, resp: Response):
        params = req.get_media()
        employee = self.service_employee.create_employee(params)
        result = {
            'result': "success",
            'id': employee.id,
            'name': employee.full_name,
        }
        resp.body = result
        resp.status = falcon.HTTP_201

    def on_get(self, req: Request, resp: Response):
        employee = self.service_employee.get_most_successfully_employees()
        result = {
            "id": employee.id,
            "full_name": employee.full_name,
            "performance": employee.performance,
            "department": employee.department_id,
        }
        resp.body = result
        resp.status = falcon.HTTP_200