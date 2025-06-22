from src.automatos.info import Info
from src.utils.impressora import Impressora

class AFD:
    def __init__(self, info: Info) -> None:
        self.info = info
        self.impressora = Impressora(self.info) 
        self.condicao_parada = True

    def computacao(self) -> bool:
        estado_atual = self.info.get_estado_inicial()
        estado_final = self.info.get_estado_final()
        funcao_transicao = self.info.get_funcao_transicao()

        while self.condicao_parada:
            simbolo_lido = self.impressora.escolher_ingrediente(estado_atual) 
            
            if simbolo_lido == "exit":
                self.condicao_parada = False
                print("\n✨ Finalizando a preparação...")
                break

            chave = (estado_atual, simbolo_lido)
            if chave in funcao_transicao:
                estado_atual = funcao_transicao[chave]
            else:
                estado_atual = 'erro'

        if estado_atual == estado_final:
            nome_da_pocao = self.info.get_nome_da_pocao()
            self.impressora.imprimir_sucesso(f'"{nome_da_pocao}" foi criada perfeitamente!')
            return True 
        else:
            self.impressora.imprimir_erro("A mistura desandou e não resultou em uma poção válida.")
            return False 
