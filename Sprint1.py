import os
from datetime import datetime, date

consultas = []

print('Inicio do App')

def nome_do_app():
    print('InovaHC')

def voltar_ao_menu_principal():
    input('\nPressione a tecla Enter para voltar ao início! ')
    main()

def exibir_opções():
    print('Escolha uma opção: ')
    print('1- Agendar consulta')
    print('2- consultas agendadas')
    print('3- cancelar consulta')
    print('4- consultas online')
    print('5- sair do app')

def escolha_de_opções():
    try:
        print()
        opção_escolhida = int(input('Escolha uma opção: '))

        if opção_escolhida == 1:
            agendar_consulta()
        elif opção_escolhida == 2:
            consultas_agendadas()
        elif opção_escolhida == 3:
            cancelar_consulta()
        elif opção_escolhida == 4:
            consultas_online()
        elif opção_escolhida == 5:
            finalizar_app()
        else:
            print('Opção inválida!')
            voltar_ao_menu_principal()
    except ValueError:
        print('Entrada inválida. Por favor, insira um número.')
        voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def agendar_consulta():
    exibir_subtitulo('Agendar consulta')
    while True:
        nome_do_paciente = input('Digite o nome do paciente: ')
        if all(c.isalpha() or c.isspace() for c in nome_do_paciente) and nome_do_paciente.strip() != "":
            break
        else:
            print("Nome inválido. Use apenas letras e espaços.")

    while True:
        data_nascimento = input('Digite a data de nascimento do paciente (dd/mm/aaaa): ')
        try:
            nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
            if nascimento > date.today():
                print("Data inválida. A data de nascimento não pode ser no futuro.")
                continue
            break
        except ValueError:
            print("Data inválida.")

    idade = date.today().year - nascimento.year

    while True:
        cpf_paciente = input('Digite o CPF do paciente (somente números): ')
        if cpf_paciente.isdigit() and len(cpf_paciente) == 11:
            break
        else:
            print("CPF inválido. O CPF deve conter 11 dígitos numéricos.")

    while True:
        data_da_consulta = input('Digite a data da consulta (dd/mm/aaaa): ')
        try:
            data_valida = datetime.strptime(data_da_consulta, '%d/%m/%Y').date()
            if data_valida < date.today():
                print("Data inválida. A data deve ser maior ou igual a de hoje.")
                continue
            break
        except ValueError:
            print("Data inválida.")

    while True:
        horario_da_consulta = input('Digite o horário da consulta (hh:mm): ')
        try:
            datetime.strptime(horario_da_consulta, '%H:%M')
            break
        except ValueError:
            print("Horário inválido.")
        
    consultas.append(f'Paciente: {nome_do_paciente}, idade: {idade} anos, CPF: {cpf_paciente}, Data: {data_da_consulta}, Horário: {horario_da_consulta}')
    
    print(f'Consulta agendada para {nome_do_paciente}, idade: {idade} anos, com o CPF: {cpf_paciente} no dia {data_da_consulta} às {horario_da_consulta}.')

    voltar_ao_menu_principal()

def consultas_agendadas():
    exibir_subtitulo('Consultas Agendadas')
    if not consultas:
        print('Nenhuma consulta agendada.')
        voltar_ao_menu_principal()
        return
    print()
    for consulta in consultas:
        print(f'- {consulta}')
    voltar_ao_menu_principal()

def cancelar_consulta():
    exibir_subtitulo('Cancelar Consulta')
    consulta_cancelada = input('Digite o nome do paciente da consulta que deseja cancelar: ')

    consultas_encontradas = [c for c in consultas if f'Paciente: {consulta_cancelada}' in c]
    if not consultas_encontradas:
        print(f'Nenhuma consulta encontrada para {consulta_cancelada}.')
        voltar_ao_menu_principal()
        return

    print('\nConsultas encontradas:')
    print()
    for i, c in enumerate(consultas_encontradas):
        print(f'Numero da consulta: {i + 1} - {c}')
    print()
    try:
        indice = int(input('Digite o número da consulta que deseja cancelar: ')) - 1
        consulta_selecionada = consultas_encontradas[indice]
        consultas.remove(consulta_selecionada)
        print()
        print('Consulta cancelada com sucesso!')
        print()
    except (ValueError, IndexError):
        print('Opção inválida.')

    voltar_ao_menu_principal()

def consultas_online():
    exibir_subtitulo('Consultas Online')

    if not consultas:
        print('Nenhuma consulta agendada no momento.')
        voltar_ao_menu_principal()
        return

    print('Consultas disponíveis para acesso online:\n')
    for i, consulta in enumerate(consultas):
        print(f'{i + 1} - {consulta}')

    try:
        escolha = int(input('\nDigite o número da consulta que deseja entrar online: ')) - 1
        if 0 <= escolha < len(consultas):
            print('\nCarregando sala online...')
            print('Acesse o link da consulta online:')
            print('https://zoom.com/abc-defg-hij') # Exemplo de link 
        else:
            print('Opção inválida. Nenhuam consulta encontrada.')
    except ValueError:
        print('Entrada inválida.')

    voltar_ao_menu_principal()


def finalizar_app():
    exibir_subtitulo('Finalizando o App...')
    print('Agradecemos por usar o InovaHC!')

def main():
    os.system('cls')
    nome_do_app()
    exibir_opções()
    escolha_de_opções()

if __name__ == '__main__':
    main()
