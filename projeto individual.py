


# Lista para os resultados dos candidatos
candidatos = []

def calcularmedia(entrevista, teorico, pratico, soft_skills):
    return (entrevista + teorico + pratico + soft_skills) / 4

def avaliaraprovacao(media):
    return "Aprovado" if media >= 7 else "Reprovado"

def adicionarcandidato():
    nome = str(input("Nome do candidato: "))
    entrevista = float(input("Nota da entrevista: "))
    teorico = float(input("Nota do teste teórico: "))
    pratico = float(input("Nota do teste prático: "))
    soft_skills = float(input("Nota de soft skills: "))

    media = calcularmedia(entrevista, teorico, pratico, soft_skills)
    resultado = avaliaraprovacao(media)

    candidato = {
        "Nome": nome,
        "Entrevista": entrevista,
        "Teórico": teorico,
        "Prático": pratico,
        "Soft Skills": soft_skills,
        "Média": media,
        "Resultado": resultado
    }

    candidatos.append(candidato)

def buscar_candidato(nome):
    for candidato in candidatos:
        if candidato["Nome"] == nome:
            print(f"Nome: {candidato['Nome']}")
            print(f"Entrevista NOTA {candidato['Entrevista']}, Teoria NOTA {candidato['Teórico']}, Prática NOTA {candidato['Prático']}, Soft NOTA {candidato['Soft Skills']}")
            print(f"Resultado: {candidato['Resultado']}")
            return

continuar = True

while continuar:
    adicionarcandidato()
    continuarresposta = input("Deseja continuar inserindo candidatos (sim/não)? ").lower()
    continuar = continuarresposta == "sim"

nomebuscar = input("Digite o nome do candidato que deseja buscar: ")
buscar_candidato(nomebuscar)
