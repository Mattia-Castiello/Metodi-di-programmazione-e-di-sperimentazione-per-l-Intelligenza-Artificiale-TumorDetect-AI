from manage.Input import Input
from dataprocessing.DropDuplicate import DropDuplicate
from dataprocessing.Standardizer import Standardizer
from dataprocessing.Bridger import Bridger
from manage.holdout import Holdout
from manage.kfoldcrossvalidation import KFoldCrossValidation
from manage.metrics import Metrics

if __name__ == '__main__':
    user_input = Input()
    user_input.get_input()

    standardization = Standardizer()
    bridger = Bridger()
    dropduplicate = DropDuplicate()

    evaluation_method = user_input.evaluation
    weight_method = user_input.weight
    chosen_metrics = user_input.metrics
    K = 1 if user_input.K is None else user_input.K
    training_perc = user_input.training / 100 # percentuale di dati da utilizzare nel set di training
    k = user_input.k

    user_input.data = dropduplicate.drop(user_input.data)
    user_input.data = bridger.impution(user_input.data)
    data, target = standardization.standardization(user_input.data)

    if(evaluation_method == 1):
        holdout = Holdout(data, target, chosen_metrics, k, weight_method, training_perc)
        true_positive, false_positive, true_negative, false_negative = holdout.evaluate()
    else:
        kfold = KFoldCrossValidation(data, target, chosen_metrics, k, weight_method, K)
        true_positive, false_positive, true_negative, false_negative = kfold.evaluate()
    
    metrics = Metrics(true_positive, true_negative, false_positive, false_negative, chosen_metrics)
    metrics.save_metrics(metrics.get_metrics(K))