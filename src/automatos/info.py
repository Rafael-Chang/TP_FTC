from src.utils.arquivo import Arquivo 
from pathlib import Path

class Info:
    def __init__(self) -> None:
        self.conjunto_estados = []
        self.estado_inicial:str  
        self.estado_final:str
        self.funcao_transicao = {}
        self.lista_simbolos = []
        self.nome_da_pocao:str

    def inicializar(self, escolha_maquina:int) -> None:
        caminho_arquivo = Arquivo().escolher_entrada(escolha_maquina)

        self.conjunto_estados, self.estado_inicial, self.estado_final, self.funcao_transicao, self.lista_simbolos = Arquivo().get_data(caminho_arquivo)

        self.set_nome_da_pocao(caminho_arquivo)
    
    def print_info(self) -> None:
        print(f"Conjunto de estados[{len(self.conjunto_estados)}]: {self.conjunto_estados}")
        print(f"Estado Inicial: {self.estado_inicial}")
        print(f"Estado Final: {self.estado_final}")
        print(f"Lista de simbolos: {self.lista_simbolos}")
        print("Função de transicao: \n")
        for (estado_origem, simbolo_lido), estado_destino in self.funcao_transicao.items():

            transicao =f""" Do estado [{estado_origem}]\n Le o simbolo [{simbolo_lido}]\n Vai para o estado [{estado_destino}]\n"""
            print(f"{transicao}")

    def get_nome_da_pocao(self)->str:
        return self.nome_da_pocao 

    def set_nome_da_pocao(self,caminho_arquivo:str)->None:
        nome_da_pocao = Path(caminho_arquivo).stem
        nome_da_pocao_f = nome_da_pocao.replace('_', ' ')
        self.nome_da_pocao = nome_da_pocao_f

    def get_lista_simbolos(self)->list:
        return self.lista_simbolos

    def get_conjunto_estados(self)->list:
        return self.conjunto_estados

    def get_funcao_transicao(self)->dict:
        return self.funcao_transicao
    
    def get_estado_inicial(self)->str:
        return self.estado_inicial

    def get_estado_final(self)->str:
        return self.estado_final

