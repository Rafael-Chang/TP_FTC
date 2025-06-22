import re
import os

class Arquivo:

    def read_arquivo(self,caminho_arquivo:str) -> list:

        with open(caminho_arquivo, 'r') as arq:
            linhas = [linha.strip() for linha in arq if linha.strip()]#lista de linhas

        arq.close()
        return linhas

    def get_data(self,caminho_arquivo:str):

        linhas = self.read_arquivo(caminho_arquivo)
        conjunto_estados = []
        estado_inicial = ""  
        estado_final = ""
        funcao_transicao = {}
        alfabeto = set() 

        i = 0
        if linhas[i].startswith("Q:"): #Se a primeira linha começa com Q
            conjunto_estados = linhas[i][2:].strip().split()
            i += 1 #Avança para a proxima linha
        else:
            raise ValueError("Arquivo com formato invalideo")

        estado_inicial = linhas[i][2:].strip()
        i += 1

        estado_final = linhas[i][2:].strip()
        i += 1

        while i < len(linhas) and linhas[i] != "---":

            linha_atual = linhas[i]
            partes = re.findall(r'(\w+)\s+->\s+(\w+)\s+\|\s+([a-zA-Z0-9 ]+)', linha_atual)

            for estado_origem, estado_destino, chars_entrada in partes:
                simbolos = chars_entrada.strip().split()
                for simbolo in simbolos:
                    chave = (estado_origem, simbolo)
                    funcao_transicao[chave] = estado_destino
                    alfabeto.add(simbolo)
            i += 1

        return conjunto_estados, estado_inicial, estado_final, funcao_transicao, list(alfabeto)

    def mostrar_entradas(self, escolha_maquina: int) -> list:
        pastas = {1: "AFD", 2: "APD", 3: "Moore", 4: "Mealy", 5: "Turing"}
        pasta = pastas.get(escolha_maquina)
        caminho_base = f"arquivos/{pasta}" 

        if not os.path.exists(caminho_base):
            print(f"❌ Diretório não encontrado: {caminho_base}")
            return []

        arquivos = [
            arq for arq in os.listdir(caminho_base)
            if arq.endswith(".txt")
        ]

        if not arquivos:
            print(f"⚠️ Nenhum arquivo .txt encontrado na pasta {caminho_base}")
            return [] 

        print(f"\n📂 Arquivos em {caminho_base}/:\n")
        for i, nome in enumerate(arquivos):
            print(f"[{i}] {nome}")
        return arquivos

    def escolher_entrada(self, escolha_maquina: int) -> str:
        arquivos = self.mostrar_entradas(escolha_maquina)
        if not arquivos:
            return ""

        try:
            escolha = int(input("\nEscolha o arquivo desejado (pelo número): "))
            if 0 <= escolha < len(arquivos):
                pasta = {1: "AFD", 2: "APD", 3: "Moore", 4: "Mealy", 5: "Turing"}[escolha_maquina]
                caminho = os.path.join("arquivos", pasta, arquivos[escolha])
                return caminho
            else:
                print("❌ Escolha inválida.")
                return self.escolher_entrada(escolha_maquina)
        except ValueError:
            print("❌ Entrada inválida.")
            return self.escolher_entrada(escolha_maquina) 
