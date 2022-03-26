from typing import Optional, List

import attr


@attr.dataclass
class BaseModel:
    pk: Optional[int] = None


@attr.dataclass
class Chat(BaseModel):
    order_date: Optional[str] = None


@attr.dataclass
class Department(BaseModel):
    name: Optional[str] = None


@attr.dataclass
class Employee(BaseModel):
    full_name: Optional[str] = None
    performance: float = None
    department_id: Department = None


if __name__ == '__main__':
    chat = Chat(pk=1, order_date='Alex')
    print(chat.__dict__)
