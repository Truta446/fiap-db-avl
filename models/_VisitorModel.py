from . import PersonModel

class VisitorModel(PersonModel):
  def __init__(
    self,
    name: str,
    birth_date: str,
    phone: str,
    email: str,
    cpf: str,
    rg: str,
    code: int,
    last_visit: str,
    address: str
  ) -> None:
    super().__init__(
      name=name,
      birth_date=birth_date,
      phone=phone,
      email=email,
      cpf=cpf,
      rg=rg,
    )
    self.code = code
    self.last_visit = last_visit
    self.address = address
