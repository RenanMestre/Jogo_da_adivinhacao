# Desenvolvido por XXXXXX
# Biblioteca para gerar números aleatórios
import random

# Mensagem de boas vindas
print("Seja bem vindo ao jogo da advinhação!\n")
nivel = 0
# Enquanto for verdadeiro permanece no jogo
while True:
    # Nível 1
    nivel = 1
    print(f"<---------------Nível {nivel}--------------->")
    # Requisição do número ao jogador
    numero = int (input("Digite um número de 1 a 5: "))

    # Condição para segurança em não permitir que o usuário digite um número menor ou maior do que foi requisitado  
    if numero >= 1 and numero <= 3:
        # Gerando e imprimindo número aleatório dentro de 1 e 5
        numero_aleatorio = random.randint(1, 5)
        print(f"Número aleatório gerado: {numero_aleatorio}\n")

        # Verificando se o usuário acertou
        if numero == numero_aleatorio:
            # Nível 2
            nivel = 2
            print("Parabéns você passou para o próxima nível!\n")
            print(f"<---------------Nível {nivel}--------------->")
            numero2 = int (input("Digite o segundo número de 6 a 10: "))
            # Condição para segurança em não permitir que o usuário digite um número menor ou maior do que foi requisitado 
            if numero2 >= 6 and numero2 <= 10:
                numero_aleatorio = random.randint(6, 10)
                print(f"Número aleatório gerado: {numero_aleatorio}\n")
                
                # Verificando se o usuário acertou e subiu de nível
                if numero2 == numero_aleatorio:
                    # Nível 3
                    nivel = 3
                    print("Parabéns você passou para o próxima nível!\n")
                    print(f"<---------------Nível {nivel}--------------->")
                    numero3 = int (input("Digite o terceiro número de 7 a 9: "))
                    

                    if numero3 >= 11 and numero3 <= 15:
                        # Gerando número aleatório dentro de 7 e 9
                        numero_aleatorio = random.randint(11, 15)
                        print(f"Número aleatório gerado: {numero_aleatorio}\n")
                        
                        # Verificando se o usuário acertou e concluíu o jogo
                        if numero3 == numero_aleatorio:
                            # Passou
                            print("Você acertou parabéns!\nVocê concluíu todos os níveis!")
                            input("Deseja jogar novamente S/N? ")
                            # Condição para verificar se o jogador quer jogar novamente
                            if resposta == 'S' or resposta == 's':
                                print("Recomeçando o jogo...\n")
                            elif resposta == 'N' or resposta == 'n' or resposta == 'S' or resposta == 's':
                                print("Jogo encerrado!\nObrigado por jogar, volte mais vezes!\n")
                                break
                            else:
                                print("Resposta incorreta!")
                        else:
                            # Não passou
                            print("Infelizmente você perdeu, não desista!\n")
                            resposta = input("Deseja continuar S/N? ").strip().upper()
                            if resposta == 'S' or resposta == 's':
                                print("Recomeçando o nível\n")
                                continue
                            elif resposta == 'N' or resposta == 'n':
                                print("Jogo encerrado!\nObrigado por jogar, volte mais vezes!\n")
                                break
                            else:
                                print("Resposta incorreta!")
                    else:
                        # Digitou número menor que 11 ou maior que 15
                        print("Número incorreto!\n")
                        continue
                else:
                    # Perdeu
                    print("Infelizmente você perdeu, não desista!\n")
                    resposta = input("Deseja continuar S/N? ").strip().upper()

                    if resposta == 'S' or resposta == 's':
                        print("Recomeçando o nível\n")
                        continue
                    elif resposta == 'N' or resposta == 'n':
                        print("Jogo encerrado!\nObrigado por jogar, volte mais vezes!\n")
                        break
                    else:
                        print("Resposta incorreta!")
            else:
                # Digitou número menor que 6 ou maior que 10
                print("Número incorreto\n")
                nivel = 2
        else:
            # Perdeu
            print("Infelizmente você perdeu, não desista!\n")
            resposta = input("Deseja continuar S/N? ").strip().upper()
            
            if resposta == 'S' or resposta == 's':
                print("Recomeçando o nível\n")
                continue
            elif resposta == 'N' or resposta == 'n':
                print("Jogo encerrado!\nObrigado por jogar, volte mais vezes!\n")
                break
            else:
                print("Resposta incorreta!")
    else:
        # Digitou número menor que 1 e maior que 5
        print("Número incorreto!\n")
        continue
else:
    # Condição de segurança para garantir a segurança do sistema
    print("Sistema encerrado!")