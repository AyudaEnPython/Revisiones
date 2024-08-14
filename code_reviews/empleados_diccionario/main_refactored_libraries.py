"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict, List, Tuple, Union
# pip install prototools
from prototools import (
    int_input,
    float_input,
    ask_to_finish,
    cyan,
    tabulate,
    text_align,
    ProtoDB,
)

Payroll = List[Dict[str, Union[str, float]]]
HEADERS = ["Id", "Name", "Department", "Salary"]


def get_id(data: Payroll) -> Tuple[bool, Union[str, None]]:
    while True:
        _id = int_input(
            "Employeed id: ", min=0, max=9999)
        _id = str(_id).rjust(4, '0')
        if _id in data:
            return True, _id
        else:
            text_align("Employee not found.")
            if not ask_to_finish():
                break
    return False, None


def update_salary(data: Payroll, _id: str, salary: float) -> None:
    data[_id]["salary"] = salary


def show(data: Payroll) -> None:
    print(tabulate(
        data=[
            [k, v["name"], v["department"], v["salary"]]
            for k, v in data.items()
        ], headers=HEADERS, color=cyan,
    ))


def main():
    employees: Payroll = ProtoDB("payroll").get_data()
    show(employees)
    ok, employee_id = get_id(employees)
    if ok:
        assert isinstance(employee_id, str)
        new_salary = float_input("Salary: ", min=0)
        update_salary(employees, employee_id, new_salary)
        text_align("Payroll updated!")
        show(employees)
    else:
        text_align("No changes were made to the payroll.")


if __name__ == "__main__":
    main()  