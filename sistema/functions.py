#Arquivo direcionado para a modularidade, todas as funções estao neste arquivo
from time import sleep

lista_medicos = [] #lista medicos
lista_pacientes = [] #lista pacientes
lista_consultas = [] #lista consultas

def cpf_valido(cpf):
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido."
    else:
        # Converte o CPF em uma lista de inteiros
        cpf = [int(digit) for digit in cpf]

        # Verifica se todos os caracteres são dígitos
        is_valid = True
        for digit in cpf:
            if digit < 0 or digit > 9:
                is_valid = False
                break

        if is_valid:
            # Calcula o primeiro dígito verificador
            soma1 = 0
            for i in range(9):
                soma1 += cpf[i] * (10 - i)
            digito1 = (soma1 * 10 % 11) % 10

            # Calcula o segundo dígito verificador
            soma2 = 0
            for i in range(10):
                soma2 += cpf[i] * (11 - i)
            digito2 = (soma2 * 10 % 11) % 10

            # Verifica se os dígitos calculados são iguais aos fornecidos
            if digito1 == cpf[9] and digito2 == cpf[10]:
                return "CPF válido."
            else:
                return "CPF inválido."
        else:
            return "CPF inválido."


def cadastrar_medico():
    nome_medico = input("Digite o nome do medico: ")
    especialidade = input("Digite a especialidade: ")
    
    if nome_medico in lista_medicos:
        print("Medico ja cadastrado!")
    else:
        medico = {'nome':nome_medico, 'especialidade':especialidade}
        lista_medicos.append(medico)
        print("Medico cadastrado com sucesso!")

def cadastrar_paciente():
    nome_paciente = input("Digite o nome do paciente: ")
    cpf_paciente = input("Digite o CPF do paciente (somentes numeros): ")
    if not cpf_valido(cpf_paciente):
        print("CPF invalido, entre com um CPF valido!")
        return
    for paciente in lista_pacientes:
        if paciente['cpf_paciente'] == cpf_paciente:
            print("Paciente já cadastrado no sistema!")
            return
        
    email_paciente = input("Digite o email do paciente: ")
    paciente = {'nome_paciente': nome_paciente, 'cpf_paciente':cpf_paciente, 'email_paciente': email_paciente}
    lista_pacientes.append(paciente)
    print("Carregando...")
    sleep(3)
    print("Paciente cadastrado com sucesso!")

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

if __name__ == "__main__":
    main()


    