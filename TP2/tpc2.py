import re

def converter_lista_numerada(texto):
    linhas = texto.split("\n")
    resultado = []
    dentro_lista = False

    for linha in linhas:
        m = re.match(r'^\d+\.\s+(.*)$', linha)

        if m:
            if not dentro_lista:
                resultado.append("<ol>")
                dentro_lista = True

            resultado.append(f"<li>{m.group(1)}</li>")

        else:
            if dentro_lista:
                resultado.append("</ol>")
                dentro_lista = False

            resultado.append(linha)

    if dentro_lista:
        resultado.append("</ol>")

    return "\n".join(resultado)


texto = """1. Primeiro item
2. Segundo item
3. Terceiro item"""

print(converter_lista_numerada(texto))