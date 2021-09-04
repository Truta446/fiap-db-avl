from . import PersonModel

class EmployeeModel(PersonModel):
  def __init__(
    self,
    name: str,
    birth_date: str,
    phone: str,
    email: str,
    cpf: str,
    rg: str,
    salary: float,
    monthly_workload: int,
    admission_date: str
  ) -> None:
    super().__init__(
      name=name,
      birth_date=birth_date,
      phone=phone,
      email=email,
      cpf=cpf,
      rg=rg,
    )
    self.salary = salary
    self.monthly_workload = monthly_workload
    self.admission_date = admission_date
