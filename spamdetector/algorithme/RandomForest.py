from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score,recall_score, f1_score,roc_auc_score


class RandomForest:
    def __init__(self, tr, path_img):
        self.lR = RandomForestClassifier()
        self.tr = tr
        self.path_img = path_img


    def result(self):
        X_train, X_test, Y_train, Y_test = self.tr.divide()
        self.lR.fit(X_train, Y_train)
        predict_lR = self.lR.predict(X_test)
        accuracy_RF = accuracy_score(Y_test, predict_lR)
        precision_RF = precision_score(Y_test, predict_lR)
        recall_RF = recall_score(Y_test, predict_lR)
        f1_score_RF = f1_score(Y_test, predict_lR)
        auc_RF = roc_auc_score(Y_test, predict_lR)
        print('accuracy ', accuracy_RF, 'precision ', precision_RF, 'recall ', recall_RF, 'f1_score ', f1_score_RF,
              'auc ', auc_RF)
