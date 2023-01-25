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

    def on_get(self, req: Request, resp: Response):
        departments = self.service_department.get_lists()
        print("departments", departments)
        resp.status = falcon.HTTP_200

    def on_put(self, req: Request, resp: Response):
        params = req.get_media()
        # pk = int(params.get('pk', 1))
        department = self.service_department.filer_by(params)
        print('department', department)
        resp.status = falcon.HTTP_200

    def on_delete(self, req: Request, resp: Response):
        params = req.get_media()
        pk = int(params.get('pk'))
        department = self.service_department.delete(pk)
        print('department', department)
        resp.status = falcon.HTTP_204

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
        result_new = self.service_employee.get_new_relations_ships()
        print('!!!!!!!!!!!!!!!', result_new)
        resp.body = result
        resp.status = falcon.HTTP_200


@component
class EmployeesNew:
    service_employee: EmployeeServiceInterface

    def on_get(self, req: Request, resp: Response):
        employees = self.service_employee.get_departments_performance_sum()
        resp.body = dict(employees)
        resp.status = falcon.HTTP_200
