import base64

senha = input("Digite a senha: ")
senha_codificada = "U2VuaGFTZWNyM3Q0"

if base64.b64encode(senha.encode('utf-8')).decode('utf-8') == senha_codificada:

    print("Senha correta!")
else:
    print("Senha incorreta!")