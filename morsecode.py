# Tradutor de código morse

# Autor => Rômulo do Carmo Sousa e Henrique Costa
# E-mails => romulocarmos@gmail.com, ryder3k.yt@gmail.com

# A ·--        0 - Zero -----                   ä·-·-               Sinal de Início -·-·
# B -···       1 - Um ·----                     æ·-·-               Iniciar Transmissão Geral -·
# C -·-·       2 - Dois ··---                   à·--·-              Iniciar Transmissão Específica -·--·
# D -··        3 - Três ···--                   å·--·-              S O S ···---···
# E ·          4 - Quatro ····-                 ç-·-··              Entendido ···-·
# F ··-·       5 - Cinco ·····                  ĉ-·-··              Entendido / Recebido / Copiado ·-·
# G --·        6 - Seis -····                   ch----              Separador dentro da mensagem -···
# H ····       7 - Sete --···                   š----               Mudar para Wabun Code -··--
# I ··         8 - Oito ---··                   ð··--·              Esperar 10 Segundos ·-···
# J ·---       9 - nove ----·                   è·-··-              Pausa -···-·
# K -·-        . - Ponto ·-·-·-                 é··-··              Fim da mensagem ·-·-·
# L ·-··       , - Vírgula --··--               đ··-··              Fim do contato ···-·
# M --         ? - Interrogação ··--··          ĝ--·-·              Saindo do ar -·-··-··
# N -·         ' - Apóstrofo ·----·             ĥ Novo----          Erro ·······
# O ---        ! - Exclamação -·-·--            ĥ Antigo-·--·       Erro · · ·
# P ·--·       / - Barra -··-·                  ĵ·---·
# Q --·-       ( - Parênteses Aberto -·--·      ñ--·-
# R ·-·        ) - Parênteses Fechado -·--·-    ö---·
# S ···                                         & - E Comercial · ···
#                                               ø---·
# T -          : - Dois Pontos ---···           ŝ···-·
# U ··-        ; - Ponto e Vírgula -·-·-·       þ·--··
# V ···-       = - Igual -···-                  ü··-
# W ·--        + - Adição ·-·-·                 ŭ··-
# X -··-       - - Hífen / Subtração -····
# Y -·--       _ - Linha Baixa ··--·
# Z --··       " - Aspas ·-··-·
#              $ - Cifrão ···-··
#              @ - Arroba ·--·-·


morse_code = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--··--',
    '!': '-·-·--', '/': '-··-·', '(': '-·--·', ')': '-·--·-', ':': '---···', ';': '-·-·-·', '=': '-···-',
    '-': '-····', '_': '··--·', '"': '·-··-·', '$': '···-··', '@': '·--·-·', '?': '··--··', '+': '·-·-·',
    "'": '·----·', 'à': '·--·-', 'ç': '-·-··', 'è': '·-··-', 'é': '..-..', '&': '· ···', ' ': ' / '

    }

morse_code = {
    '.-': 'a', '-...': 'b', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    '..': 'i', '.---': 'j', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    '--.-': 'q', '.-.': 'r', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    '-.--': 'y', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '.....': '5', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--··--',
    '-·-·--':'!' , '/': '-··-·', '(': '-·--·', ')': '-·--·-', ':': '---···', ';': '-·-·-·', '=': '-···-',
    '-····': '-', '_': '··--·', '"': '·-··-·', '$': '···-··', '@': '·--·-·', '?': '··--··', '+': '·-·-·',
    '·----·': "'", 'à': '·--·-', 'ç': '-·-··', 'è': '·-··-', 'é': '..-..', '&': '· ···', ' ': ' / '

        }
    
# Codifica a string
def encode(text):
    text = text.strip().lower()  # A função strip retira espaços vasios do inicio e fim da string e lower converte para minusculo
    texto_cod = ''

    # Valida cada item do texto
    for i in text:
        if i == '&':
            texto_cod = texto_cod + '. ...'

        elif i not in morse_code:
            texto_cod = texto_cod + '/ '

        else:
            texto_cod = texto_cod + morse_code[i] + ' '

    return texto_cod    
