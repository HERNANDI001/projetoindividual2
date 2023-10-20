


# Função para obter a avaliação de uma etapa do processo
def obter_avaliacao(etapa):
    try:
        avaliacao = float(input(f"Digite a avaliação para {etapa}: "))
        return avaliacao
    except ValueError:
        print("Por favor, insira um valor numérico.")
        return obter_avaliacao(etapa)

# Lista de etapas do processo
etapas = ["entrevista", "teste teórico", "teste prático", "avaliação de soft skills"]

# Inicializa um dicionário para armazenar as avaliações
avaliacoes = {}

# Coleta as avaliações para cada etapa do processo
for etapa in etapas:
    avaliacao = obter_avaliacao(etapa)
    avaliacoes[etapa] = avaliacao

# Constrói a string no formato desejado
resultado = "e{}_t{}_p{}_s{}".format(
    avaliacoes["entrevista"],
    avaliacoes["teste teórico"],
    avaliacoes["teste prático"],
    avaliacoes["avaliação de soft skills"]
)

# Imprime a string formatada
print("Resultado: " + resultado)



# Função para coletar avaliações de um candidato
def coletar_avaliacoes():
    avaliacoes = {}
    etapas = ["entrevista", "teste teórico", "teste prático", "avaliação de soft skills"]
    for etapa in etapas:
        avaliacao = float(input(f"Digite a avaliação para {etapa}: "))
        avaliacoes[etapa] = avaliacao
    return avaliacoes

# Função para adicionar um candidato à lista
def adicionar_candidato(lista, nome, avaliacoes):
    candidato = f"{nome}: e{avaliacoes['entrevista']}_t{avaliacoes['teste teórico']}_p{avaliacoes['teste prático']}_s{avaliacoes['avaliação de soft skills']}"
    lista.append(candidato)

# Função para buscar candidatos com base nos critérios
def buscar_candidatos(lista, critrios):
    candidatos_selecionados = []
    for candidato in lista:
        if all(crit in candidato for crit in critrios):
            candidatos_selecionados.append(candidato)
    return candidatos_selecionados

# Lista para armazenar os resultados
resultados = []

# Coletar informações do candidato
nome = input("Digite o nome do candidato: ")
avaliacoes = coletar_avaliacoes()

# Adicionar candidato à lista
adicionar_candidato(resultados, nome, avaliacoes)

# Solicitar critérios de busca ao usuário
critrios = input("Digite os critérios de busca (por exemplo, 'eX_tX' para buscar candidatos com essas avaliações): ").split('_')

# Realizar a busca
candidatos_selecionados = buscar_candidatos(resultados, critrios)

# Exibir os candidatos que atendem aos critérios
if candidatos_selecionados:
    print("Candidatos encontrados:")
    for candidato in candidatos_selecionados:
        print(candidato)
else:
    print("Nenhum candidato encontrado com os critérios especificados.")

