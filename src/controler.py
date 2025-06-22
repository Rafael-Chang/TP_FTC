from src.utils.menu import Menu
from src.automatos.info import Info
from src.automatos.AFD import AFD

class Controler:

    def __init__(self):
        self.menu = Menu()
        self.info = Info()

    def inicializar(self) -> int:
        escolha = self.menu.show()
        self.info.inicializar(escolha)
        return escolha

    def controler_maquina(self):
        escolha = self.inicializar()
        match int(escolha):
            case 1:
                afd = AFD(self.info)
                afd.computacao()
                
            case 2:
                print("APD")
            case 3:
                print("Touring")
            case 4:
                print("Moore")
            case 5:
                print("Melay")
