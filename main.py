import json

from controllers import AttendedController, DonorController, EmployeeController, VisitorController, VolunteerController
from models import AttendedModel, DonorModel, EmployeeModel, VisitorModel, VolunteerModel

def main() -> None:
  attended_controller = AttendedController()
  donor_controller = DonorController()
  employee_controller = EmployeeController()
  visitor_controller = VisitorController()
  volunteer_controller = VolunteerController()

  with open('to-read.json', mode='r', encoding='utf8') as f:
    data = json.load(f)

  for i in data['attended']:
    attended = AttendedModel(
      name=i.get('name'),
      birth_date=i.get('birth_date'),
      phone=i.get('phone'),
      email=i.get('email'),
      cpf=i.get('cpf'),
      rg=i.get('rg'),
      family_income=i.get('family_income'),
      qty_children=i.get('qty_children'),
      is_employed=i.get('is_employed'),
    )
    attended_controller.create(attended)

  for i in data['donors']:
    donor = DonorModel(
      name=i.get('name'),
      birth_date=i.get('birth_date'),
      phone=i.get('phone'),
      email=i.get('email'),
      cpf=i.get('cpf'),
      rg=i.get('rg'),
      code=i.get('code'),
      last_visit=i.get('last_visit'),
      address=i.get('address'),
    )
    donor_controller.create(donor)

  for i in data['employees']:
    employee = EmployeeModel(
      name=i.get('name'),
      birth_date=i.get('birth_date'),
      phone=i.get('phone'),
      email=i.get('email'),
      cpf=i.get('cpf'),
      rg=i.get('rg'),
      salary=i.get('salary'),
      monthly_workload=i.get('monthly_workload'),
      admission_date=i.get('admission_date'),
    )
    employee_controller.create(employee)

  for i in data['visitors']:
    visitor = VisitorModel(
      name=i.get('name'),
      birth_date=i.get('birth_date'),
      phone=i.get('phone'),
      email=i.get('email'),
      cpf=i.get('cpf'),
      rg=i.get('rg'),
      code=i.get('code'),
      last_visit=i.get('last_visit'),
      address=i.get('address'),
    )
    visitor_controller.create(visitor)

  for i in data['volunteers']:
    volunteer = VolunteerModel(
      name=i.get('name'),
      birth_date=i.get('birth_date'),
      phone=i.get('phone'),
      email=i.get('email'),
      cpf=i.get('cpf'),
      rg=i.get('rg'),
      code=i.get('code'),
      department=i.get('department'),
      address=i.get('address'),
    )
    volunteer_controller.create(volunteer)

  main_opt = 1

  while main_opt:
    opt1 = menu()
    opt2 = sub_menu()

    if opt1 == 1:
      if opt2 == 1:
        attended_controller.find()
      elif opt2 == 2:
        donor_controller.find()
      elif opt2 == 3:
        employee_controller.find()
      elif opt2 == 4:
        visitor_controller.find()
      else:
        volunteer_controller.find()
    elif opt1 == 2:
      if opt2 == 1:
        print(attended_controller.show_in_order())
      elif opt2 == 2:
        print(donor_controller.show_in_order())
      elif opt2 == 3:
        print(employee_controller.show_in_order())
      elif opt2 == 4:
        print(visitor_controller.show_in_order())
      else:
        print(volunteer_controller.show_in_order())
    elif opt1 == 3:
      name = str(input('\nDigite um nome para buscar: '))

      if opt2 == 1:
        count, data = attended_controller.find_by_name(name)

        if count:
          print('O nome inserido foi encontrado com sucesso.')
          print(f'\nNome: {data.name}\nCPF: {data.cpf}\nRG: {data.rg}\nData de Nascimento: {data.birth_date}\nE-mail: {data.email}\nCelular: {data.phone}\nRenda familiar: {str(data.family_income)}\nQuantidade de filhos: {str(data.qty_children)}\nEstá empregado: {"Sim" if data.is_employed else "Não"}')
          print(f'\nQuantidade de comparações realizadas: {count}')
        else:
          print('\nNão encontramos o nome inserido.')
      elif opt2 == 2:
        count, data = donor_controller.find_by_name(name)

        if count:
          print('O nome inserido foi encontrado com sucesso.')
          print(f'\nNome: {data.name}\nCPF: {data.cpf}\nRG: {data.rg}\nData de Nascimento: {data.birth_date}\nE-mail: {data.email}\nCelular: {data.phone}\nCódigo: {str(data.code)}\nÚltima visita: {data.last_visit}\nEndereço: {data.address}')
          print(f'\nQuantidade de comparações realizadas: {count}')
        else:
          print('\nNão encontramos o nome inserido.')
      elif opt2 == 3:
        count, data = employee_controller.find_by_name(name)

        if count:
          print('O nome inserido foi encontrado com sucesso.')
          print(f'\nNome: {data.name}\nCPF: {data.cpf}\nRG: {data.rg}\nData de Nascimento: {data.birth_date}\nE-mail: {data.email}\nCelular: {data.phone}\nSalário: {str(data.salary)}\nCarga horária mensal: {str(data.monthly_workload)} horas\nEstá empregado: {data.admission_date}')
          print(f'\nQuantidade de comparações realizadas: {count}')
        else:
          print('\nNão encontramos o nome inserido.')
      elif opt2 == 4:
        count, data = visitor_controller.find_by_name(name)

        if count:
          print('O nome inserido foi encontrado com sucesso.')
          print(f'\nNome: {data.name}\nCPF: {data.cpf}\nRG: {data.rg}\nData de Nascimento: {data.birth_date}\nE-mail: {data.email}\nCelular: {data.phone}\nCódigo: {str(data.code)}\nÚltima visita: {data.last_visit}\nEndereço: {data.address}')
          print(f'\nQuantidade de comparações realizadas: {count}')
        else:
          print('\nNão encontramos o nome inserido.')
      else:
        count, data = volunteer_controller.find_by_name(name)

        if count:
          print('O nome inserido foi encontrado com sucesso.')
          print(f'\nNome: {data.name}\nCPF: {data.cpf}\nRG: {data.rg}\nData de Nascimento: {data.birth_date}\nE-mail: {data.email}\nCelular: {data.phone}\nCódigo: {str(data.code)}\nDepartamento: {data.last_visit}\nEndereço: {data.address}')
          print(f'\nQuantidade de comparações realizadas: {count}')
        else:
          print('\nNão encontramos o nome inserido.')
    elif opt1 == 4:
      name = str(input('Nome: '))
      birth_date = str(input('Data de nascimento: '))
      phone = str(input('Celular: '))
      email = str(input('E-mail: '))
      cpf = str(input('CPF: '))
      rg = str(input('RG: '))

      if opt2 == 1:
        family_income = float(input('Renda familiar: '))
        qty_children = int(input('Quantidade de filhos: '))
        is_employed = int(input('Empregado (1 - Sim; 0 - Não): '))
        is_employed = False if is_employed == 0 else True

        payload = AttendedModel(
          name=name,
          birth_date=birth_date,
          phone=phone,
          email=email,
          cpf=cpf,
          rg=rg,
          family_income=family_income,
          qty_children=qty_children,
          is_employed=is_employed,
        )
        attended_controller.create(payload)
      elif opt2 == 2:
        code = int(input('Código: '))
        last_visit = str(input('Última visita: '))
        address = str(input('Endereço: '))

        payload = DonorModel(
          name=name,
          birth_date=birth_date,
          phone=phone,
          email=email,
          cpf=cpf,
          rg=rg,
          code=code,
          last_visit=last_visit,
          address=address,
        )
        donor_controller.create(payload)
      elif opt2 == 3:
        salary = float(input('Salário: '))
        monthly_workload = int(input('Canga horária mensal: '))
        admission_date = str(input('Data de admissão: '))

        payload = EmployeeModel(
          name=name,
          birth_date=birth_date,
          phone=phone,
          email=email,
          cpf=cpf,
          rg=rg,
          salary=salary,
          monthly_workload=monthly_workload,
          admission_date=admission_date,
        )
        employee_controller.create(payload)
      elif opt2 == 4:
        code = int(input('Código: '))
        last_visit = str(input('Última visita: '))
        address = str(input('Endereço: '))

        payload = VisitorModel(
          name=name,
          birth_date=birth_date,
          phone=phone,
          email=email,
          cpf=cpf,
          rg=rg,
          code=code,
          last_visit=last_visit,
          address=address,
        )
        visitor_controller.create(payload)
      else:
        code = int(input('Código: '))
        department = str(input('Departamento: '))
        address = str(input('Endereço: '))

        payload = VolunteerModel(
          name=name,
          birth_date=birth_date,
          phone=phone,
          email=email,
          cpf=cpf,
          rg=rg,
          code=code,
          department=department,
          address=address,
        )
        volunteer_controller.create(payload)

      print('\nDados inseridos com sucesso!')
    elif opt1 == 5:
      name = str(input('\nDigite um nome para atualizar: '))

      if opt2 == 1:
        count, _ = attended_controller.find_by_name(name)
      elif opt2 == 2:
        count, _ = donor_controller.find_by_name(name)
      elif opt2 == 3:
        count, _ = employee_controller.find_by_name(name)
      elif opt2 == 4:
        count, _ = visitor_controller.find_by_name(name)
      else:
        count, _ = volunteer_controller.find_by_name(name)

      if count > 0:
        birth_date = str(input('Data de nascimento: '))
        phone = str(input('Celular: '))
        email = str(input('E-mail: '))
        cpf = str(input('CPF: '))
        rg = str(input('RG: '))

        if opt2 == 1:
          family_income = float(input('Renda familiar: '))
          qty_children = int(input('Quantidade de filhos: '))
          is_employed = int(input('Empregado (1 - Sim; 0 - Não): '))
          is_employed = False if is_employed == 0 else True

          payload = AttendedModel(
            name=name,
            birth_date=birth_date,
            phone=phone,
            email=email,
            cpf=cpf,
            rg=rg,
            family_income=family_income,
            qty_children=qty_children,
            is_employed=is_employed,
          )
          attended_controller.update(payload)
        elif opt2 == 2:
          code = int(input('Código: '))
          last_visit = str(input('Última visita: '))
          address = str(input('Endereço: '))

          payload = DonorModel(
            name=name,
            birth_date=birth_date,
            phone=phone,
            email=email,
            cpf=cpf,
            rg=rg,
            code=code,
            last_visit=last_visit,
            address=address,
          )
          donor_controller.update(payload)
        elif opt2 == 3:
          salary = float(input('Salário: '))
          monthly_workload = int(input('Canga horária mensal: '))
          admission_date = str(input('Data de admissão: '))

          payload = EmployeeModel(
            name=name,
            birth_date=birth_date,
            phone=phone,
            email=email,
            cpf=cpf,
            rg=rg,
            salary=salary,
            monthly_workload=monthly_workload,
            admission_date=admission_date,
          )
          employee_controller.update(payload)
        elif opt2 == 4:
          code = int(input('Código: '))
          last_visit = str(input('Última visita: '))
          address = str(input('Endereço: '))

          payload = VisitorModel(
            name=name,
            birth_date=birth_date,
            phone=phone,
            email=email,
            cpf=cpf,
            rg=rg,
            code=code,
            last_visit=last_visit,
            address=address,
          )
          visitor_controller.update(payload)
        else:
          code = int(input('Código: '))
          department = str(input('Departamento: '))
          address = str(input('Endereço: '))

          payload = VolunteerModel(
            name=name,
            birth_date=birth_date,
            phone=phone,
            email=email,
            cpf=cpf,
            rg=rg,
            code=code,
            department=department,
            address=address,
          )
          volunteer_controller.update(payload)

        print('\nDados atualizados com sucesso!')
      else:
        print('\nNão encontramos o nome inserido.')
    else:
      name = str(input('\nDigite um nome para deletar: '))

      if opt2 == 1:
        attended_controller.delete_by_name(name)
        attended_controller.find()
      elif opt2 == 2:
        donor_controller.delete_by_name(name)
        donor_controller.find()
      elif opt2 == 3:
        employee_controller.delete_by_name(name)
        employee_controller.find()
      elif opt2 == 4:
        visitor_controller.delete_by_name(name)
        visitor_controller.find()
      else:
        volunteer_controller.delete_by_name(name)
        volunteer_controller.find()

      print('\nDados deletados com sucesso!')

    main_opt = int(input('\nDeseja continuar? (0 - Não; 1 - Sim): '))

def menu() -> int:
  print('\nMenu')
  print('\n1 - Listar árvore;')
  print('\n2 - Listar nomes ordenados;')
  print('\n3 - Listar um cadastro;')
  print('\n4 - Inserir novo cadastro;')
  print('\n5 - Atualizar um cadastro;')
  print('\n6 - Deletar um cadastro;')

  opt = 0

  while opt > 6 or opt < 1:
    opt = int(input('\n\nEscolha uma opção: '))

  return opt

def sub_menu() -> int:
  print('\nCategoria')
  print('\n1 - Atendente;')
  print('\n2 - Doador;')
  print('\n3 - Funcionário;')
  print('\n4 - Visitante;')
  print('\n5 - Voluntário;')

  opt = 0

  while opt > 5 or opt < 1:
    opt = int(input('\n\nEscolha uma categoria: '))

  return opt

if __name__ == "__main__":
  main()
