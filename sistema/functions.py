#Arquivo direcionado para a modularidade, todas as funções estao neste arquivo
from time import sleep

lista_medicos = [] #lista medicos
lista_pacientes = [] #lista pacientes
lista_consultas = [] #lista consultas

def cpf_valido(cpf):
    # Verifica se o CPF tem 11 dígitos e é numérico
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    # Converte o CPF em uma lista de inteiros
    cpf = [int(digit) for digit in cpf]

    # Verifica se todos os caracteres são dígitos válidos (de 0 a 9)
    for digit in cpf:
        if digit < 0 or digit > 9:
            return False

    # Calcula o primeiro dígito verificador
    soma1 = sum(cpf[i] * (10 - i) for i in range(9))
    digito1 = (soma1 * 10 % 11) % 10

    # Calcula o segundo dígito verificador
    soma2 = sum(cpf[i] * (11 - i) for i in range(10))
    digito2 = (soma2 * 10 % 11) % 10

    # Verifica se os dígitos calculados são iguais aos fornecidos
    return digito1 == cpf[9] and digito2 == cpf[10]

# funçao de cadastrar medico
def cadastrar_medico():
    nome_medico = input("Digite o nome do médico: ")
    especialidade = input("Digite a especialidade: ")
    credencial_medico = input("Digite a credencial do médico: ")
    limite_atendimentos = int(input("Quantos pacientes o médico pode atender por dia: "))

    # Verifica se o médico já foi cadastrado
    for medico in lista_medicos:
        if medico['credencial'] == credencial_medico:
            print("Médico já cadastrado no sistema!")
            return

    medico = {
        'nome': nome_medico,
        'credencial': credencial_medico,
        'especialidade': especialidade,
        'limite_atendimento': limite_atendimentos
    }

    lista_medicos.append(medico)
    print("Carregando...")
    sleep(1)
    print("Médico cadastrado com sucesso!")

#funçao de cadastrar paciente
def cadastrar_paciente():
    nome_paciente = input("Digite o nome do paciente: ")
    cpf_paciente = input("Digite o CPF do paciente (somentes numeros): ")

    if not cpf_valido(cpf_paciente): #verifica se o cpf é valido usando a funçao cpf_valido
        print("CPF invalido, entre com um CPF valido!")
        return
    
    for paciente in lista_pacientes:
        if paciente['cpf_paciente'] == cpf_paciente:
            print("Paciente já cadastrado no sistema!")
            return
        
    email_paciente = input("Digite o email do paciente: ")
    paciente = {'nome_paciente': nome_paciente, 
                'cpf_paciente':cpf_paciente, 
                'email_paciente': email_paciente}
    
    lista_pacientes.append(paciente)
    print("Carregando...")
    sleep(1)
    print("Paciente cadastrado com sucesso!")

def listar_medicos():
    for medico in lista_medicos:
        print(f"Medicos disponiveis no consultorio: {medico}")

def verificar_limite_consultas(medico_escolhido, dia_consulta):
    # Cria uma lista vazia para contar as consultas do dia
    consultas_do_dia = []

    # Verifica cada consulta na lista de consultas
    for consulta in lista_consultas:
        # Se o médico e o dia da consulta correspondem, adiciona à lista
        if consulta['medico_escolhido'] == medico_escolhido and consulta['dia_consulta'] == dia_consulta:
            consultas_do_dia.append(consulta)

    # Procura o médico na lista de médicos
    medico = None
    for med in lista_medicos:
        if med['nome'] == medico_escolhido:
            medico = med
            break

    # Se encontrou o médico e o número de consultas do dia for menor que o limite, retorna True
    if medico is not None and len(consultas_do_dia) < medico['limite_atendimento']:
        print("Consulta cadastrada")
        return True
    
    # Se não encontrou o médico ou já atingiu o limite, retorna False
    print("Medico atingiu o maximo de consultas!")
    return False


def agendar_consulta():
    nome_paciente = input("Digite o nome do paciente: ")
    cpf_paciente = input("Digite o CPF do paciente (somentes numeros): ")
    for paciente in lista_pacientes:
        if paciente['cpf_paciente'] == cpf_paciente and paciente['nome_paciente'] == nome_paciente:
            print("Paciente já cadastrado no sistema!")
            paciente_cadastrado = True
            break
    if not paciente_cadastrado:
        cadastrar_paciente()
    #CONTINUA O AGENDAMENTO DA CONSULTA
    print("Carregando médicos disponíveis no consultório...")
    sleep(1)
    listar_medicos()

    medico_escolhido = input("Com que médico deseja se consultar: ")

    if medico_escolhido not in [medico['nome'] for medico in lista_medicos]:
        print("Médico indisponível no consultório!")
        return

    dia_consulta = input("Qual o dia da consulta: ")

    # Verifica o limite de consultas do médico no dia
    if not agendar_consulta(medico_escolhido, dia_consulta):
        print("Este médico já atingiu o limite de consultas para o dia!")
        return

    hora_consulta = input("Qual o horário da consulta: ")
    consulta = {
        'nome_paciente': nome_paciente,
        'cpf_paciente': cpf_paciente,
        'medico_escolhido': medico_escolhido,
        'dia_consulta': dia_consulta,
        'hora_consulta': hora_consulta
    }
    lista_consultas.append(consulta)
    print("Consulta agendada com sucesso!")
    

    
def main():
    while True:   
        print("\n=== Sistema de Controle de Consultas ===")
        print("1 - Cadastrar medico")
        print("2 - Cadastrar paciente")
        print("3 - Agendar consulta")
        print("4 - Listar consultas")
        print("5 - Excluir consultas")
        print("0 - sair do programa")

        opcao = input("Digite a opção: ")
        if opcao == "1":
            cadastrar_medico()
        elif opcao == "2":
            cadastrar_paciente()
        elif opcao == "3":
            agendar_consulta()


if __name__ == "__main__":
    main()


    