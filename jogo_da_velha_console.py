#!/usr/bin/env python3
"""
Jogo da Velha - Versão Console
Jogo simples com X e O no terminal
"""

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [' '] * 9
        self.jogador_atual = 'X'
    
    def mostrar_tabuleiro(self):
        print("\n   |   |   ")
        print(f" {self.tabuleiro[0]} | {self.tabuleiro[1]} | {self.tabuleiro[2]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.tabuleiro[3]} | {self.tabuleiro[4]} | {self.tabuleiro[5]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.tabuleiro[6]} | {self.tabuleiro[7]} | {self.tabuleiro[8]} ")
        print("   |   |   \n")
    
    def mostrar_posicoes(self):
        print("Posições do tabuleiro:")
        print("\n   |   |   ")
        print(" 1 | 2 | 3 ")
        print("___|___|___")
        print("   |   |   ")
        print(" 4 | 5 | 6 ")
        print("___|___|___")
        print("   |   |   ")
        print(" 7 | 8 | 9 ")
        print("   |   |   \n")
    
    def fazer_jogada(self, posicao):
        if 1 <= posicao <= 9 and self.tabuleiro[posicao - 1] == ' ':
            self.tabuleiro[posicao - 1] = self.jogador_atual
            return True
        return False
    
    def verificar_vencedor(self):
        # Combinações vencedoras
        combinacoes = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
            [0, 4, 8], [2, 4, 6]              # Diagonais
        ]
        
        for combo in combinacoes:
            if (self.tabuleiro[combo[0]] == self.tabuleiro[combo[1]] == 
                self.tabuleiro[combo[2]] != ' '):
                return self.tabuleiro[combo[0]]
        return None
    
    def tabuleiro_cheio(self):
        return ' ' not in self.tabuleiro
    
    def trocar_jogador(self):
        self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'
    
    def jogar(self):
        print("🎮 BEM-VINDO AO JOGO DA VELHA! 🎮")
        print("Jogador X começa!")
        self.mostrar_posicoes()
        
        while True:
            self.mostrar_tabuleiro()
            print(f"Vez do jogador {self.jogador_atual}")
            
            try:
                posicao = int(input("Digite a posição (1-9) ou 0 para sair: "))
                
                if posicao == 0:
                    print("Jogo encerrado!")
                    break
                
                if not self.fazer_jogada(posicao):
                    print("❌ Posição inválida ou já ocupada!")
                    continue
                
                vencedor = self.verificar_vencedor()
                if vencedor:
                    self.mostrar_tabuleiro()
                    print(f"🎉 JOGADOR {vencedor} VENCEU! 🎉")
                    break
                
                if self.tabuleiro_cheio():
                    self.mostrar_tabuleiro()
                    print("🤝 EMPATE! 🤝")
                    break
                
                self.trocar_jogador()
                
            except ValueError:
                print("❌ Digite apenas números!")
            except KeyboardInterrupt:
                print("\nJogo encerrado!")
                break

def main():
    while True:
        jogo = JogoDaVelha()
        jogo.jogar()
        
        try:
            jogar_novamente = input("\nJogar novamente? (s/n): ").lower()
            if jogar_novamente != 's':
                print("Obrigado por jogar! 👋")
                break
        except KeyboardInterrupt:
            print("\nTchau! 👋")
            break

if __name__ == "__main__":
    main()