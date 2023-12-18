
    
    
    
    def __lt__(self, outraData):
        return (self.__ano, self.__mes, self.__dia) < (outraData.__ano, outraData.__mes, outraData.__dia)
    
    # Comparação para maior que entre duas datas
    def __gt__(self, outraData):
        return (self.__ano, self.__mes, self.__dia) > (outraData.__ano, outraData.__mes, outraData.__dia)

# Definindo uma classe abstrata para análise de dados
class AnaliseDados(ABC): 
    @abstractmethod
    def entrada_de_dados(self):
        pass

    @abstractmethod
    def mostra_mediana(self):
        pass
    
    @abstractmethod
    def mostra_menor(self):
        pass

    @abstractmethod
    def mostra_maior(self):
        pass
    
    @abstractmethod
    def listar_em_ordem(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass

# Classe para lidar com listas de nomes, herdando de AnaliseDados
class ListaNomes(AnaliseDados):
    def __init__(self):
        self.__lista = []        

    # Método para inserir nomes na lista
    def entrada_de_dados(self):
        try:
            quantidade = int(input("Quantos nomes deseja inserir? "))
            for _ in range(quantidade):
                nome = input("Digite o nome: ")
                self.__lista.append(no
