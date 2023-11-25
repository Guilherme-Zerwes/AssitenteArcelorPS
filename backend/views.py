from flask import Blueprint, request, send_file, send_from_directory
from flask_cors import cross_origin
import input
import json

view = Blueprint(__name__, 'view')

@view.route('/')
@cross_origin()
def home():
    print('acessado')
    return '<p>Hello world</p>'

@view.route('/input')
# @cross_origin()
def voice_input():
    response = {'input': input.record_audio()}
    return response

@view.route('/chat-response', methods=['POST'])
def chat_response():
    question_num = request.json['number']
    # with open('answers.json') as f:
    #     response = json.load(f)
    response = answers

    if question_num > len(response):
        response = {"response": "De nada, foi um prazer te ajudar!"}
    else:
        response = {"response": response[str(question_num)]}
    return response

answers = {
    "1": """Bom dia, sou o ArcelorPS_GPT, o chatbot criado por Guilherme Zerwes para a etapa de dinâmica do processo seletivo da Arcelormittal Tubarão.
    \n Como posso te ajudar hoje?""",
    "2": """Claro aqui está uma pequena apresentação sobre o Guilherme:
        \n Nome - Guilherme Zerwes, 
        \n Idade - 21 anos, 
        \n Local de Residência - Vitória, ES
        \n \n Guilherme é um jovem estudante de engenharia mecânica na UFES com interesses nas áreas de programação e projetos mecânicos.
        Algumas de suas qualidades são sua dedicação e disciplina com seus deveres: ele sempre se esforça para entregar bons resultados! Além disso ele também é uma pessoa bem flexível, isto é, ele consegue se adaptar bem para atender várias situações diferentes, sejam demandas de trabalho ou de colaboração em equipe.""",

    "3": """Posso falar das experiências do Guilherme sim. Aqui está um pequeno resumo de algumas de suas experiências mais recentes: 
    \n Em 2021 ele já trabalhou como freelancer com Python na empresa Upwork. Lá, ele aprendeu a melhorar suas habilidades de programação, além de realizar contato direto com cliente e lidar com prazos e requisitos de projetos.
    \n Em 2023 ele realizou um intercâmbio acadêmico para Arts et Métiers e desenvolveu um software com ferramentas de inteligência artificial para auxiliar nos projetos de pesquisa dos laboratórios adjuntos a faculdade. Nesse período, ele aprendeu um pouco mais sobre o mundo da inteligência artificial e lidou com os desafios de trabalhar em uma nova língua e interagir em um time multicultural.""",

    "4": """Claro! Durante a faculdade o Guilherme esteve muito envolvido, desde o início da graduação, no projeto chamado Vitória Baja.
    \n Durante seus 3 anos nesse projeto, que acompanha a criação e fabricação de um carro de competição, ele esteve em cargos diferentes, o que garantiu que ele aprendesse sobre várias áreas. Ele aprendeu várias habilidades técnicas referentes à processos de fabricação como soldagem, usinagem, torneamento. Além disso, ele desenvolveu vários projetos com ferramentas CAD em 3D e 2D. E também utilizou softwares para elaborar apresentações, planilhas de análises, simulações, entre outros. Já na parte interpessoal, ele se tornou lider do projeto de suspensão e direção, então desenvolveu suas habilidades de liderança, comunicação, trabalhar sob a pressão da competição e em equipe.
    \n Ele também buscou se aprimorar em outra área que ele tem interesse que é a programação, tendo feito alguns cursos e projetos individuais para aprender mais sobre análise de dados, machine learning e inteligência artificial.""",
    
    "5": """O Guilherme também tem outros interesses além desses: ele gosta bastante de música e teatro, sempre que pode ele tenta assistir peças e apresentações de orquestras. Ele gosta também de caminhadas na natureza, fazer trilhas, acampamentos."""
}