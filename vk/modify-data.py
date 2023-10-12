import json
import os
import msvcrt
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

data = []
exercises = []

with open('api-data-questions.json', encoding='utf-8-sig') as f:
    data = json.load(f)
    f.close()

exercises = data['exercicios']


def addCategory():
    os.system('cls')
    while (input("Adicionar nova categoria? (S/n) ").capitalize() == "S"):
        os.system('cls')
        category = input("Nome da categoria: ")
        categoryDifficulty = input("Dificuldade: ")
        if category == "" or categoryDifficulty == "":
            print("Categoria ou dificuldade vazios")
            return
        questionList = []
        if not category in exercises:
            exercises[category] = {}
        if not categoryDifficulty in exercises[category]:
            exercises[category][categoryDifficulty] = {}
        else:
            questionList = exercises[category][categoryDifficulty]
        while (input(
                str(len(questionList)) +
            (" questão - " if len(questionList) == 1 else " questões - ") +
                "Adicionar novo enunciado? (S/n) ").capitalize() == "S"):
            os.system('cls')
            _correct = ""
            _wrong = []
            _answers = []
            _tempQuestion = {}
            _question = input("Enunciado: ")
            print("Respostas: ")
            _answers.append(input())
            while (input("Adicionar nova resposta? (S/n) ").capitalize() == "S"
                   ):
                os.system('cls')
                print("Enunciado: " + _question)
                print("Respostas: ")
                for i in range(len(_answers)):
                    print(str(i + 1) + "- " + _answers[i])
                _answers.append(input())
            os.system('cls')
            print("Enunciado: " + _question)
            print("Respostas: ")
            for i in range(len(_answers)):
                print(str(i + 1) + "- " + _answers[i])
            _correctIdx = int(input("Número da resposta correta: ")) - 1
            _correct = _answers[_correctIdx]
            _wrong = _answers[:_correctIdx] + _answers[_correctIdx + 1:]
            _tempQuestion['enunciado'] = _question
            _tempQuestion['resposta_correta'] = _correct
            _tempQuestion['respostas_erradas'] = _wrong
            _tempQuestion['respostas'] = _answers
            questionList.append(_tempQuestion)
        exercises[category][categoryDifficulty] = questionList


def modifyCategoryMenu():
    os.system('cls')
    opt = 0
    print(
        "1- Remover questão\n2- Mudar nome da categoria\n3- Mudar dificuldade\n4- Excluir categoria\n5- Excluir dificuldade\n6- Voltar"
    )
    try:
        opt = int(input())
    except:
        opt = -1
    if opt == 1:
        removeQuestion()
        pass
    elif opt == 2:
        modifyCategoryName()
    elif opt == 3:
        modifyCategoryDifficulty()
    elif opt == 4:
        deleteCategory()
    elif opt == 5:
        deleteCategoryDifficulty()
    elif opt == 6:
        return True
    else:
        print("Opção inválida!")


def removeQuestion():
    os.system('cls')
    print("-- Categorias --")
    for i in exercises.keys():
        print(i)
    category = input("\nNome da categoria: ")
    if not category in exercises:
        print("Categoria inexistente")
        return
    os.system('cls')
    print("-- Dificuldades --")
    for i in exercises[category].keys():
        print(i)
    categoryDifficulty = input("\nDificuldade: ")
    if not categoryDifficulty in exercises[category]:
        print("Dificuldade inexistente")
        return
    questionList = exercises[category][categoryDifficulty]
    if not categoryDifficulty in exercises[category]:
        print("Dificuldade inexistente")
        return
    for i in range(0, len(questionList)):
        print(
            str(i + 1) + "- " + questionList[i]['enunciado'] + " -",
            questionList[i]['respostas'])
    try:
        _questionIdx = int(input("Número da questão que quer excluir: ")) - 1
    except:
        print("Número inválido")
        return
    questionList.pop(_questionIdx)


def modifyCategoryName():
    os.system('cls')
    print("-- Categorias --")
    for i in exercises.keys():
        print(i)
    old_name = input("\nNome da categoria: ")
    if not old_name in exercises:
        print("Categoria inexistente ou nome inválido")
        return
    new_name = input("Novo nome para a categoria: ")
    if new_name == "":
        print("Nome inválido")
        return
    exercises[new_name] = exercises.pop(old_name)


def modifyCategoryDifficulty():
    os.system('cls')
    print("-- Categorias --")
    for i in exercises.keys():
        print(i)
    category = input("\nNome da categoria: ")
    if not category in exercises:
        print("Categoria inexistente")
        return
    os.system('cls')
    print("-- Dificuldades --")
    for i in exercises[category].keys():
        print(i)
    old_diff = input("\nDificuldade que quer alterar: ")
    if not old_diff in exercises[category]:
        print("Dificuldade inexistente")
        return
    new_diff = input("Nova dificuldade: ")
    if new_diff == "":
        print("Dificuldade inválida")
        return
    exercises[category][new_diff] = exercises[category].pop(old_diff)


def deleteCategory():
    os.system('cls')
    print("-- Categorias --")
    for i in exercises.keys():
        print(i)
    category = input("\nNome da categoria que quer excluir: ")
    if not category in exercises:
        print("Categoria inexistente")
        return
    exercises.pop(category)


def deleteCategoryDifficulty():
    os.system('cls')
    print("-- Categorias --")
    for i in exercises.keys():
        print(i)
    category = input("\nNome da categoria que quer excluir: ")
    if not category in exercises:
        print("Categoria inexistente")
        return
    os.system('cls')
    print("-- Dificuldades --")
    for i in exercises[category].keys():
        print(i)
    difficulty = input("\nDificuldade que quer excluir: ")
    if not difficulty in exercises[category]:
        print("Dificuldade inexistente")
        return
    exercises[category].pop(difficulty)


def checkContinue():
    inputed = input("\nContinuar com o programa? (S/n) ").capitalize()
    if inputed != "S" and inputed != "N":
        print("Opção inválida, pressione qualquer tecla para continuar")
        msvcrt.getch()
        inputed = "S"
    if (inputed.capitalize() == "S"):
        return True
    else:
        return False


def viewStructure():
    os.system('cls')
    for i in exercises.keys():
        print(f"{i}{Style.RESET_ALL}")
        for j in exercises[i].keys():
            print(f"{Fore.LIGHTBLACK_EX}   ╚═ {Style.RESET_ALL}{j}")
            print(
                f"{Fore.LIGHTBLACK_EX}      ╚═ {Style.RESET_ALL}{len(exercises[i][j])}",
                "questão" if len(exercises[i][j]) == 1 else "questões")


def main():
    contProg = True
    opt = 0
    while (contProg):
        os.system('cls')
        print(
            "1- Adicionar novas categorias / questões\n2- Modificar categoria existente\n3- Visualizar estrutura"
        )
        try:
            opt = int(input())
        except:
            opt = -1
        if opt == 1:
            addCategory()
        elif opt == 2:
            if modifyCategoryMenu() == True:
                continue
        elif opt == 3:
            viewStructure()
        else:
            print("Opção inválida!")
        contProg = checkContinue()


main()

with open('api-data-questions.json', 'w', encoding='utf-8-sig') as fw:
    json.dump(data, fw, ensure_ascii=False)