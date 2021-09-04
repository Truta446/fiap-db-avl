import sys
from typing import List, Tuple

class AVLService:
  def __init__(self, node: dict = None):
    self.node = node
    self.indexChildren(None, None)

  def indexChildren(self, left, right) -> None:
    self.left = left
    self.right = right

  def balance(self) -> int:
    depth_left = 0

    if self.left:
      depth_left = self.left.depth()

    depth_right = 0

    if self.right:
      depth_right = self.right.depth()

    return depth_left - depth_right

  def depth(self) -> int:
    depth_left = 0

    if self.left and self.left.node:
      depth_left = self.left.depth()

    depth_right = 0

    if self.right and self.right.node:
      depth_right = self.right.depth()

    return 1 + max(depth_left, depth_right)

  def lrotate(self) -> None:
    self.node, self.right.node = self.right.node, self.node
    old_left = self.left
    self.indexChildren(self.right, self.right.right)
    self.left.indexChildren(old_left, self.left.left)

  def rrotate(self) -> None:
    self.node, self.left.node = self.left.node, self.node
    old_right = self.right
    self.indexChildren(self.left.left, self.left)
    self.right.indexChildren(self.right.right, old_right)

  def lrrotate(self) -> None:
    self.left.lrotate()
    self.rrotate()

  def rlrotate(self) -> None:
    self.right.rrotate()
    self.lrotate()

  def perform_balance(self) -> None:
    bal = self.balance()

    if bal > 1:
      if self.left.balance() > 0:
        self.rrotate()
      else:
        self.lrrotate()
    elif bal < -1:
      if self.right.balance() < 0:
        self.lrotate()
      else:
        self.rlrotate()

  def logical_successor(self, successor: dict) -> dict:
    if successor and not successor.left:
      return successor

    return self.logical_successor(successor.left)

  def logical_predecessor(self, predecessor: dict) -> dict:
    if predecessor and not predecessor.right:
      return predecessor

    return self.logical_predecessor(predecessor.right)

  def insert(self, node: dict) -> None:
    if self.node == None:
      self.node = node
    elif node.name <= self.node.name:
      if not self.left:
        self.left = AVLService(node)
      else:
        self.left.insert(node)
    else:
      if not self.right:
        self.right = AVLService(node)
      else:
        self.right.insert(node)

    self.perform_balance()

  def display(self, indent: str, last: bool) -> None:
    if self.node != None:
      sys.stdout.write(indent)

      if last:
        sys.stdout.write("R----")
        indent += "     "
      else:
        sys.stdout.write("L----")
        indent += "|    "

      print(self.node.name)

      if self.left:
        self.left.display(indent, False)

      if self.right:
        self.right.display(indent, True)

  def search(self, name: str, count: int = 0) -> Tuple[int, dict]:
    if not self.node:
      return 0, None
    elif self.node.name == name:
      return count + 1, self.node
    elif self.node.name < name:
      if self.right == None:
        return 0, None

      return self.right.search(name, count + 1)

    if self.left == None:
      return 0, None

    return self.left.search(name, count + 1)

  def delete(self, name: str) -> None:
    if self.node:
      if self.node.name == name:
        if not self.left and not self.right:
          self.node = None
        elif self.left and not self.left.node:
          self.node = self.right.node
        elif self.right and not self.right.node:
          self.node = self.left.node
        else:
          if self.left:
            replacement = self.logical_predecessor(self.left)

            if replacement != None:
              self.node.name = replacement.node.name
              self.left.delete(replacement.node.name)
          else:
            replacement = self.logical_successor(self.right)

            if replacement != None:
              self.node.name = replacement.node.name
              self.right.delete(replacement.node.name)
      elif name < self.node.name:
        self.left.delete(name)
      elif name > self.node.name:
        self.right.delete(name)

      self.perform_balance()

  def update(self, node: dict) -> None:
    if self.node:
      if self.node.name == node.name:
        self.node = node
      elif(self.node.name < node.name):
        if self.right == None:
          return

        return self.right.update(node)
      else:
        if self.left == None:
          return

        return self.left.update(node)

  def inorder_traverse(self) -> List[str]:
    if self.node == None:
      return []

    inlist = []

    if self.left:
      l = self.left.inorder_traverse()

      for i in l:
        inlist.append(i)


    inlist.append(self.node.name)

    if self.right:
      l = self.right.inorder_traverse()
      for i in l:
        inlist.append(i)


    return inlist
