import re

texto = """
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
"""

tokens = [
    ("COMENTARIO", r'\#.*'),
    ("VARIAVEL", r'\?[a-zA-Z0-9]+'),
    ("LINGUA", r'@[a-zA-Z]{2}'),
    ("STRING", r'"[^"]*"'),
    ("LIMIT", r'LIMIT'),
    ("NUMERO", r'[0-9]+'),
    ("DELIMITADOR", r'[{}.]'),
    ("IDENTIFICADOR", r'[a-zA-Z0-9]+'),
    ("SKIP", r'[ \t\n]+')
]

regex = "|".join(
    f"(?P<{nome}>{padrao})"
    for nome, padrao in tokens
)

for match in re.finditer(regex, texto):
    tipo = match.lastgroup
    valor = match.group()

    if tipo not in ("COMENTARIO", "SKIP"):
        print(tipo, valor)