from manage.Input import Input
from dataprocessing.DropDuplicate import DropDuplicate
from dataprocessing.Standardizer import Standardizer
from dataprocessing.Bridger import Bridger
from manage.holdout import Holdout
from manage.kfoldcrossvalidation import KFoldCrossValidation

def prepare_data(input_data):
    # Prepara i dati eliminando duplicati, eseguendo l'imputazione e la standardizzazione
    drop_duplicate = DropDuplicate()
    input_data = drop_duplicate.drop(input_data)
    input_data = Bridger().impution(input_data)
    return Standardizer().standardization(input_data)

if __name__ == '__main__':
    # Ottieni input dall'utente
    user_input = Input()
    user_input.get_input()

    # Estrapola i parametri di input
    evaluation_method = user_input.evaluation
    weight_method = user_input.weight
    chosen_metrics = user_input.metrics
    K = user_input.K if user_input.K is not None else 1
    training_percentage = user_input.training / 100
    k = user_input.k

    try:
        # Prepara i dati
        data, target = prepare_data(user_input.data)

        # Esegue la valutazione in base al metodo scelto
        if evaluation_method == 1:
            holdout = Holdout(data, target, chosen_metrics, k, weight_method, training_percentage)
            holdout.evaluate()
        else:
            kfold = KFoldCrossValidation(data, target, chosen_metrics, k, weight_method, K)
            kfold.evaluate()

    except Exception as e:
        # Gestisce eventuali eccezioni
        print("An error occurred:", str(e))
