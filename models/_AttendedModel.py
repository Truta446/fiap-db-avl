from . import PersonModel

class AttendedModel(PersonModel):
  def __init__(
    self,
    name: str,
    birth_date: str,
    phone: str,
    email: str,
    cpf: str,
    rg: str,
    family_income: float,
    qty_children: int,
    is_employed: bool
  ) -> None:
    super().__init__(
      name=name,
      birth_date=birth_date,
      phone=phone,
      email=email,
      cpf=cpf,
      rg=rg,
    )
    self.family_income = family_income
    self.qty_children = qty_children
    self.is_employed = is_employed
