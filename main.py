from manage.Input import Input
from dataprocessing.DropDuplicate import DropDuplicate
from dataprocessing.Standardizer import Standardizer
from dataprocessing.Bridger import Bridger

if __name__ == '__main__':
    user_input = Input()
    user_input.get_input()
    standardization = Standardizer()
    bridger = Bridger()
    dropduplicate = DropDuplicate()

    evaluation_method = user_input.evaluation
    chosen_metrics = user_input.metrics
    K = user_input.K

    training_perc = user_input.training
    k = user_input.k

    user_input.data = dropduplicate.drop(user_input.data)
    user_input.data = standardization.standardization(user_input.data)
    user_input.data = bridger.impution(user_input.data)

    #evaluation = Evaluation(evaluation_method, training_perc, chosen_metrics)