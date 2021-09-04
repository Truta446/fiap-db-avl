class PersonModel(object):
  def __init__(
    self,
    name: str,
    birth_date: str,
    phone: str,
    email: str,
    cpf: str,
    rg: str
  ) -> None:
    self.name = name
    self.birth_date = birth_date
    self.phone = phone
    self.email = email
    self.cpf = cpf
    self.rg = rg
