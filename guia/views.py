from django.shortcuts import render

def home(request):
    # Home agora herda o base.html via home.html
    return render(request, "guia/home.html")

def preview_procedure(request):
    # Dados fictícios só para visualizar o layout do detalhe
    context = {
        "procedure": {
            "titulo": "Licença Maternidade",
            "sei_url": "https://sei.exemplo.gov.br/processo/123",
            "descricao": "Benefício concedido à servidora gestante nos termos da legislação vigente.",
        },
        "passos": [
            {"ordem": 1, "texto": "Preencher o formulário no SEI."},
            {"ordem": 2, "texto": "Anexar documentos comprobatórios."},
            {"ordem": 3, "texto": "Aguardar análise da PGDP."},
        ],
        "bases_legais": [
            {"titulo": "Lei 8.112/1990, art. 207", "link": "#"},
            {"titulo": "Decreto X/XXXX", "link": "#"},
        ],
        "documentos": [
            {"nome": "Formulário padrão", "link": "#"},
            {"nome": "Documento comprobatório", "link": "#"},
        ],
        "faq": [
            {"pergunta": "Quem tem direito?", "resposta": "Servidoras gestantes conforme legislação."},
            {"pergunta": "Qual o prazo?", "resposta": "Conforme regras específicas e análise da PGDP."},
        ],
    }
    return render(request, "guia/procedure_detail.html", context)

def procedures_list(request):
    q = request.GET.get("q", "").strip().lower()
    cat = request.GET.get("cat", "").strip().lower()

    # Dados fictícios para ver a listagem
    base = [
        {
            "titulo": "Solicitar Férias",
            "categoria": "ferias",
            "descricao": "Como solicitar férias pelo SEI.",
            "sei_url": "https://sei.exemplo.gov.br/processo/456",
        },
        {
            "titulo": "Afastamento por Motivo de Saúde",
            "categoria": "afastamentos",
            "descricao": "Passo a passo do afastamento médico.",
            "sei_url": "",
        },
        {
            "titulo": "Auxílio-Transporte",
            "categoria": "beneficios",
            "descricao": "Documentos e regras para concessão.",
            "sei_url": "https://sei.exemplo.gov.br/processo/789",
        },
        {
            "titulo": "Nomeação e Posse",
            "categoria": "admissao",
            "descricao": "Fluxo de nomeação de servidores.",
            "sei_url": "",
        },
    ]

    itens = base
    if q:
        itens = [p for p in itens if q in p["titulo"].lower() or q in p.get("descricao","").lower()]
    if cat:
        itens = [p for p in itens if p.get("categoria","").lower() == cat]

    ctx = {"procedimentos": itens, "q": q, "cat": cat}
    return render(request, "guia/procedures_list.html", ctx)
