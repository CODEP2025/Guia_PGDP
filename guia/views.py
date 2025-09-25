from django.shortcuts import render

def home(request):
    return render(request, "guia/index.html")

def preview_procedure(request):
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
