from abc import ABC, abstractmethod
#Classa astratta Reader la quale dichiara il metodo parse
class Reader(ABC):
    @abstractmethod
    #il metodo pass prende in ingresso il nome di un qualsiasi dataset
    def parse(self, filename):
        pass


