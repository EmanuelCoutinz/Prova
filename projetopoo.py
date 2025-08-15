from bancodedados import listadecliente


class cliente:
  
  def __init__(self, nome, telefone, email, IDunico):
    self.nome = nome
    self.telefone = telefone
    self.email = email
    self.IDunico = IDunico

class reserva:

  def __init__(self,nome ,donodareserva, quartoreservado, datadecheckin, datadecheckout, statusdereserva):

    self.nome = nome
    self.donodareserva = donodareserva
    self.quartoreservado = quartoreservado
    self.datadecheckin = datadecheckin
    self.datadecheckout = datadecheckout
    self.statusdereserva = statusdereserva

class quarto:
   
   def __init__(self, numerodoquarto, tipodoquarto, preçopordiaria, statusdedisponibilidade):
     
     self.numerodoquarto = numerodoquarto
     self.tipodoquarto = tipodoquarto
     self.preçopordiaria = preçopordiaria
     self.statusdedisponibilidade = statusdedisponibilidade

class gerenciadordereservas: 
  
  def __init__(self, ver):
    
     
      