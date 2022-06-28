from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (QHBoxLayout, QLabel)
from PyQt5.QtGui import QPixmap

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        
        self.ui.textBrowser.append("... Добро пожаловать!")
        self.ui.textBrowser_2.append("... Анализ данных")
        
        self.ui.pushButton.clicked.connect(self.download_click)
        self.ui.pushButton_2.clicked.connect(self.combo)
        self.ui.pushButton_8.clicked.connect(self.clear_tab1)
        self.ui.pushButton_9.clicked.connect(self.clear_tab2)
        self.ui.pushButton_3.clicked.connect(self.optimization)
        self.ui.pushButton_10.clicked.connect(self.show_columns)
        self.ui.pushButton_7.clicked.connect(self.combo2)
        self.ui.pushButton_4.clicked.connect(self.glavny_comp)
        self.ui.pushButton_6.clicked.connect(self.openDialog)
        
    def openDialog(self):
        pass
        dialog = ClssDialog(self)
        dialog.exec_()

    def clear_tab2(self):
        self.ui.textBrowser_2.clear()
        self.ui.textBrowser_2.append("... Анализ данных")

    def clear_tab1(self):
        self.ui.textBrowser.clear()
        self.ui.textBrowser.append("... Добро пожаловать!")
# =============================================================================
# TAB1
# =============================================================================
    def download_click(self):
        
        
        
        
        try:
            file = QFileDialog.getOpenFileName(self, 'Загрузка файла', 'C:\\users\\nikit\\.spyder-py3', "Excel Files (*.xls *.xlsx *csv)")
            self.file_new = file[0]

            self.ui.textBrowser.append("... Расположение загруженного файла:")
            self.ui.textBrowser.append(self.file_new)
            
            self.file_pd = pd.read_csv(self.file_new)
            obj = self.file_pd.select_dtypes([np.object])
            obj = obj.columns[0]
            self.file_pd = self.file_pd.drop(str(obj), axis = 1)
            
            self.ui.pushButton_2.setEnabled(True)
            self.ui.pushButton_3.setEnabled(True)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_6.setEnabled(True)
            self.ui.pushButton_7.setEnabled(True)
            self.ui.pushButton_10.setEnabled(True)
            
        except:
            self.ui.textBrowser.append("... Файл не был загружен!")
        
    
    def combo(self):
        option = self.ui.comboBox.currentIndex()
        
        if option == 0:
            self.ui.textBrowser.append("... Вы выбрали 'Проверить на пропущенные значения':")
            self.ui.textBrowser.append("... Справка: Если все значения 0, то пропущенных значний нет")
            self.miss()
        elif option == 1:
            self.ui.textBrowser.append("... Вы выбрали 'Показать количество строк и столбцов':")
            self.row_columns()
        
    def optimization(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Успешно!")
        msg.setInformativeText('Датасет оптизимизораван для дальнейшей работы!')
        msg.setWindowTitle("Информация")
        msg.exec_()
        
        self.ui.textBrowser.append("... Датасет опитимизирован")
        
        self.file_pd = self.file_pd.dropna()
    
    def miss(self):
        missing = self.file_pd.isnull().sum()
        self.ui.textBrowser.append(str(missing))
        
    def row_columns(self):
        row_columns = self.file_pd.shape
        row = row_columns[0]
        columns = row_columns[1]
        self.ui.textBrowser.append("... Строк:")
        self.ui.textBrowser.append(str(row))
        self.ui.textBrowser.append("... Столбцов:")
        self.ui.textBrowser.append(str(columns))
# =============================================================================
# TAB2
# =============================================================================
    def show_columns(self):
        self.ui.textEdit.setDisabled(False)
        self.ui.textEdit_2.setDisabled(False)
        self.ui.textBrowser_2.append("... Столбцы и их номер:")
        i = 0
        while i < self.file_pd.shape[1]:
            self.ui.textBrowser_2.append(str(("[%s]"% (i) + self.file_pd.columns[i])))
            i = i + 1
        pass
        
        self.ui.textBrowser_2.append("... Для дальнейшего анализа введите номер столбца в поля [X] и [Y]")
    
    def combo2(self):
        option1 = self.ui.comboBox_2.currentIndex()
        
        if option1 == 0:
            self.ui.textBrowser_2.append("... Вы выбрали 'Показать коэффициент корреляции':")
            self.correl()
        elif option1 == 1:
            self.ui.textBrowser_2.append("... Вы выбрали 'Показать коэффициент ковариации:")
            self.covar()
        elif option1 == 2:
            self.ui.textBrowser_2.append("... Вы выбрали 'Показать коэффициент детерминации:")
            self.determ()
            
    
    def correl(self):
        X = self.ui.textEdit.toPlainText()
        Y = self.ui.textEdit_2.toPlainText()
        
        corr = self.file_pd[self.file_pd.columns[int(X)]].corr(self.file_pd[self.file_pd.columns[int(Y)]])
        self.ui.textBrowser_2.append("... Коэффициент корреляции:")
        self.ui.textBrowser_2.append(str(corr))
        pass
    
    def covar(self):
        X = self.ui.textEdit.toPlainText()
        Y = self.ui.textEdit_2.toPlainText()
        
        covv = self.file_pd[self.file_pd.columns[int(X)]].cov(self.file_pd[self.file_pd.columns[int(Y)]])
        self.ui.textBrowser_2.append("... Коэффициент ковариации:")
        self.ui.textBrowser_2.append(str(covv))
        pass
    
    def determ(self):
        self.ui.textBrowser_2.append("Детерминация")
        pass
    
    def glavny_comp(self):
        x = StandardScaler().fit_transform(self.file_pd)
        pca = PCA(n_components=2)
        principalComponents = pca.fit_transform(x)
        principalDf = pd.DataFrame(data = principalComponents
                      , columns = ['principal component 1', 'principal component 2'])
        
        self.ui.textBrowser_2.append("... Выборка после снижения размерности 'метод главных компенент':")
        self.ui.textBrowser_2.append(str(principalDf))
        
        X = principalDf.iloc[:, :-1].values
        y = principalDf.iloc[:, 1].values
        
        linear_regressor = LinearRegression()
        linear_regressor.fit(X, y)
        Y_pred = linear_regressor.predict(X)
        
        plt.scatter(X, y)
        plt.plot(X, Y_pred, color='red')
        plt.title(r'График линейной регрессии', fontsize=20)
        plt.xlabel('ось X')
        plt.ylabel('ось Y')
        plt.savefig("plot.png", format='png', dpi=150, bbox_inches='tight')

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        regressor = LinearRegression()
        regressor.fit(X_train, y_train)
        determ = regressor.score(X_train, y_train)

        y_pred = regressor.predict(X_test)

        data = pd.DataFrame(y_test, columns = ["Actual"])
        data1 = pd.DataFrame(y_pred, columns = ["Predicted"])

        frame = pd.concat([data, data1], axis = 1)
        self.ui.textBrowser_2.append("... Предсказанные данные:")
        self.ui.textBrowser_2.append(str(frame))
        
        self.ui.textBrowser_2.append("... Коэфицент корреляции:")
        cor = principalDf['principal component 1'].corr(principalDf['principal component 2'])
        self.ui.textBrowser_2.append(str(cor))
        
        self.ui.textBrowser_2.append("... Коэфицент детерминации:")
        self.ui.textBrowser_2.append(str(determ))
        
        self.ui.textBrowser_2.append("... Доля от общей дисперсии:")
        self.ui.textBrowser_2.append(str(pca.explained_variance_ratio_))
        
        self.ui.textBrowser_2.append("... Модель предсказывает ответ" + " " + str(regressor.intercept_) + " " + "при Х равном нулю")
        self.ui.textBrowser_2.append("... Предсказанный ответ возрастет до" + " " + str(regressor.coef_) + " " + "при Х увеличенным на еденицу")
        
        self.ui.textBrowser_2.append("... Среднее значение абсолютного значения ошибок (MAE):")
        self.ui.textBrowser_2.append(str(metrics.mean_absolute_error(y_test, y_pred)))
        self.ui.textBrowser_2.append("... Среднее значение квадратов ошибок (MSE):")
        self.ui.textBrowser_2.append(str(metrics.mean_squared_error(y_test, y_pred)))
        self.ui.textBrowser_2.append("... Квадратный корень из MSE (RMSE):")
        self.ui.textBrowser_2.append(str(np.sqrt(metrics.mean_squared_error(y_test, y_pred))))
        
        
        
        
        
        pass
    
class ClssDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog, self).__init__(parent)  
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("plot.png")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.move(100, 200)
        self.setWindowTitle('График')
        self.show()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(693, 596)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 691, 411))
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(10, 50, 271, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 50, 93, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(10, 90, 671, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(522, 50, 161, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab)
        self.pushButton_8.setGeometry(QtCore.QRect(590, 10, 93, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 10, 161, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 50, 271, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 130, 671, 251))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setGeometry(QtCore.QRect(520, 50, 161, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setGeometry(QtCore.QRect(290, 50, 91, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(590, 90, 93, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(80, 10, 51, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setDisabled(True)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(160, 20, 71, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 10, 51, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setDisabled(True)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setEnabled(False)
        self.pushButton_10.setGeometry(QtCore.QRect(290, 10, 121, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(180, 10, 321, 61))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_3, "")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(-420, 700, 300, 200))
        self.openGLWidget.setObjectName("openGLWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 410, 691, 141))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setPixmap(QtGui.QPixmap("cbb.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 693, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Загрузить файл"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Проверить на пропущенные значения"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Показать количество строк и столбцов"))
        self.pushButton_2.setText(_translate("MainWindow", "Выполнить"))
        self.pushButton_3.setText(_translate("MainWindow", "Оптимизировать датасет"))
        self.pushButton_8.setText(_translate("MainWindow", "Отчистить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Загрузка"))
        self.pushButton_4.setText(_translate("MainWindow", "Снизить размерность"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Показать коэффициент корреляции"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Показать коэффициент ковариации"))
        self.pushButton_6.setText(_translate("MainWindow", "Показать график"))
        self.pushButton_7.setText(_translate("MainWindow", "Выполнить"))
        self.label_2.setText(_translate("MainWindow", "Столбец X"))
        self.pushButton_9.setText(_translate("MainWindow", "Отчистить"))
        self.label_3.setText(_translate("MainWindow", "Столбец Y"))
        self.pushButton_10.setText(_translate("MainWindow", "Показать столбцы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Анализ"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Работу выполнил:</span></p><p align=\"center\"><span style=\" font-size:10pt;\">Фадеев Никита, группа 4391-21</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Справка"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
    

