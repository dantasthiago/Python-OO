class Cpf:
  def __init__(self, documento):
    documento = str(documento)
    if self.cpf_valido(documento):
      self.cpf = documento
    else:
      raise ValueError("CPF inválido!")

  def cpf_valido(self, documento):
    if len(documento) == 11:
      return True
    else:
      return False
    
  def __str__(self):
    return self.format_cpf()

  def format_cpf(self):
    fatia_dois = self.cpf[3:6]
    fatia_tres = self.cpf[6:9]
    fatia_quatro = self.cpf[9:]
    fatia_um = self.cpf[0:3]
    return(
      '{}.{}.{}-{}'.format(
      fatia_um,
      fatia_dois,
      fatia_tres,
      fatia_quatro
      )
    )