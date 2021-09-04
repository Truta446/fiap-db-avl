from typing import List, Tuple

from models import VolunteerModel
from services import AVLService

class VolunteerController(object):
  def __init__(self):
    self.db = AVLService()

  def show_in_order(self) -> List[str]:
    return self.db.inorder_traverse()

  def find(self) -> List[VolunteerModel]:
    return self.db.display("", True)

  def find_by_name(self, name: str) -> Tuple[int, VolunteerModel]:
    return self.db.search(name=name)

  def create(self, data: VolunteerModel) -> None:
    self.db.insert(node=data)

  def update(self, data: VolunteerModel) -> None:
    self.db.update(node=data)

  def delete_by_name(self, name: str) -> None:
    self.db.delete(name=name)
