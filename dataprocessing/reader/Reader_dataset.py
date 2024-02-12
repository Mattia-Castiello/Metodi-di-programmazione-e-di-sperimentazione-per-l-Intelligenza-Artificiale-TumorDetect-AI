from abc import ABC, abstractmethod
#Classa astratta Reader la quale dichiara il metodo parse
class Reader_dataset(ABC):
    """
           Metodo astratto per analizzare un dataset e restituire i dati.

           Parameters:
           filename (str): Nome del file del dataset.

           Returns:
           Dipende dall'implementazione delle sotto classi.
    """
    @abstractmethod
    #il metodo pass prende in ingresso il nome di un qualsiasi dataset
    def parse(self, filename):
        pass


