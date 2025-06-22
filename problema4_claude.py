import random
import os

class SorteioPersonalizado:
    def __init__(self):
        self.premios = []
        self.participantes = []
        self.resultados = []
    
    def exibir_logo(self):
        """Exibe uma logo ASCII genérica"""
        logo = """
        ╔═══════════════════════════════════════╗
        ║          🎉 SORTEIO PREMIADO 🎉       ║
        ║                                       ║
        ║     ★ ★ ★ FESTAS & EVENTOS ★ ★ ★     ║
        ╚═══════════════════════════════════════╝
        """
        print(logo)
    
    def cadastrar_premios(self):
        """Cadastra os prêmios do sorteio"""
        print("\n=== CADASTRO DE PRÊMIOS ===")
        print("Digite ao menos 2 prêmios:")
        
        while len(self.premios) < 2:
            premio = input(f"Digite o {len(self.premios) + 1}º prêmio: ").strip()
            if premio:
                self.premios.append(premio)
                print(f"✓ Prêmio '{premio}' cadastrado!")
            else:
                print("⚠️ Digite um nome válido para o prêmio!")
        
        # Permite cadastrar mais prêmios se desejar
        while True:
            continuar = input("\nDeseja cadastrar mais um prêmio? (s/n): ").lower()
            if continuar == 's':
                premio = input(f"Digite o {len(self.premios) + 1}º prêmio: ").strip()
                if premio:
                    self.premios.append(premio)
                    print(f"✓ Prêmio '{premio}' cadastrado!")
            else:
                break
        
        print(f"\n✅ Total de {len(self.premios)} prêmios cadastrados:")
        for i, premio in enumerate(self.premios, 1):
            print(f"   {i}. {premio}")
    
    def cadastrar_participantes(self):
        """Cadastra os participantes do sorteio"""
        print("\n=== CADASTRO DE PARTICIPANTES ===")
        print("Digite ao menos 5 participantes:")
        
        while len(self.participantes) < 5:
            nome = input(f"Digite o nome do {len(self.participantes) + 1}º participante: ").strip()
            if nome:
                if nome not in self.participantes:
                    self.participantes.append(nome)
                    print(f"✓ Participante '{nome}' cadastrado!")
                else:
                    print("⚠️ Este nome já foi cadastrado!")
            else:
                print("⚠️ Digite um nome válido!")
        
        # Permite cadastrar mais participantes se desejartGP
        while True:
            continuar = input("\nDeseja cadastrar mais um participante? (s/n): ").lower()
            if continuar == 's':
                nome = input(f"Digite o nome do {len(self.participantes) + 1}º participante: ").strip()
                if nome and nome not in self.participantes:
                    self.participantes.append(nome)
                    print(f"✓ Participante '{nome}' cadastrado!")
                elif nome in self.participantes:
                    print("⚠️ Este nome já foi cadastrado!")
            else:
                break
        
        print(f"\n✅ Total de {len(self.participantes)} participantes cadastrados:")
        for i, nome in enumerate(self.participantes, 1):
            print(f"   {i}. {nome}")
    
    def realizar_sorteios(self):
        """Realiza os sorteios consecutivos"""
        print("\n" + "="*50)
        print("🎲 INICIANDO SORTEIOS!")
        print("="*50)
        
        participantes_disponiveis = self.participantes.copy()
        
        # Realizar sorteios baseados no número de prêmios disponíveis
        num_sorteios = min(len(self.premios), len(self.participantes))
        
        for i in range(num_sorteios):
            if not participantes_disponiveis:
                break
                
            print(f"\n🎯 SORTEIO {i + 1}:")
            print(f"Prêmio: {self.premios[i]}")
            print(f"Participantes concorrendo: {len(participantes_disponiveis)}")
            
            input("\n🔄 Pressione ENTER para sortear...")
            
            # Usar random.random() para garantir aleatoriedade
            indice_sorteado = int(random.random() * len(participantes_disponiveis))
            ganhador = participantes_disponiveis[indice_sorteado]
            
            # Remover ganhador da lista para próximo sorteio
            participantes_disponiveis.remove(ganhador)
            
            # Armazenar resultado
            resultado = {
                'sorteio': i + 1,
                'premio': self.premios[i],
                'ganhador': ganhador
            }
            self.resultados.append(resultado)
            
            # Exibir resultado
            print(f"\n🎉 RESULTADO DO {i + 1}º SORTEIO:")
            print(f"🏆 PRÊMIO: {self.premios[i]}")
            print(f"👤 GANHADOR: {ganhador}")
            print("-" * 40)
    
    def exibir_resultados_finais(self):
        """Exibe o resumo final dos sorteios"""
        print("\n" + "="*50)
        print("📋 RESUMO FINAL DOS SORTEIOS")
        print("="*50)
        
        if not self.resultados:
            print("❌ Nenhum sorteio foi realizado!")
            return
        
        for resultado in self.resultados:
            print(f"\n🏆 {resultado['sorteio']}º SORTEIO:")
            print(f"   Prêmio: {resultado['premio']}")
            print(f"   Ganhador: {resultado['ganhador']}")
        
        print("\n🎊 PARABÉNS A TODOS OS GANHADORES! 🎊")
    
    def iniciar_aplicativo(self):
        """Método principal que coordena todo o fluxo do aplicativo"""
        os.system('clear' if os.name == 'posix' else 'cls')  # Limpa a tela
        
        self.exibir_logo()
        
        print("\n🎉 Bem-vindo ao Sistema de Sorteios Personalizados!")
        print("Este aplicativo permite realizar sorteios justos e aleatórios.")
        
        try:
            # Fase 1: Cadastro de prêmios
            self.cadastrar_premios()
            
            # Fase 2: Cadastro de participantes
            self.cadastrar_participantes()
            
            # Fase 3: Confirmação antes do sorteio
            print("\n" + "="*50)
            print("📊 RESUMO PRÉ-SORTEIO:")
            print(f"Prêmios: {len(self.premios)}")
            print(f"Participantes: {len(self.participantes)}")
            print(f"Sorteios que serão realizados: {min(len(self.premios), len(self.participantes))}")
            
            iniciar = input("\n🚀 Tudo pronto! Deseja iniciar os sorteios? (s/n): ").lower()
            
            if iniciar == 's':
                # Fase 4: Realizar sorteios
                self.realizar_sorteios()
                
                # Fase 5: Exibir resultados finais
                self.exibir_resultados_finais()
            else:
                print("❌ Sorteio cancelado pelo usuário.")
        
        except KeyboardInterrupt:
            print("\n\n❌ Aplicativo interrompido pelo usuário.")
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")

def main():
    """Função principal do programa"""
    sorteio = SorteioPersonalizado()
    sorteio.iniciar_aplicativo()

if __name__ == "__main__":
    main()