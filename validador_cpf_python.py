def cpf_validate(cpf):

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return "invalido"

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    if cpf == cpf[::-1]:
        return "invalido"

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = 0
        for num in range(0, i):
            value += int(cpf[num]) * ((i+1) - num)
        digit = ((value * 10) % 11) % 10
        if digit != int(cpf[i]):
            return "invalido"
    return "valido"