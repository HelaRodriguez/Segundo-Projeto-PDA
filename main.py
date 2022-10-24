nome = "Xarge"
situacao = "Dores de Cabeça"
horarioChegada = "12:33"
historico = "sem doenças cronicas"
idade = 31
classificacao = "Azul"

print("paciente: ",nome," idade: ",idade)
print("horario de chegada: ",horarioChegada)
print(historico)
print("Classificado como: ", classificacao)

if classificacao == "Vermelho":   
  print("Atendimento imediato")
  
elif classificacao == "Laranja":
  print("Atendimento dentro de 10 minutos")

elif classificacao == "Amarelo":
  print("Atendimento dentro de 30 minutos")

elif classificacao == "Verde":
  print("Atendimento dentro de 50 a 60 minutos")

elif classificacao == "Azul":
  ("Atendimento dentro de 70 a 80 minutos")