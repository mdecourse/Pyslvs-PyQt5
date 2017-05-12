# -*- coding: utf-8 -*-
from ..QtModules import *
from .Ui_run_Path_Solving import Ui_Form as PathSolving_Form
from ..graphics.ChartGraphics import ChartDialog
from .run_Path_Solving_progress import Path_Solving_progress_show
from .run_Path_Solving_series import Path_Solving_series_show

class Path_Solving_show(QWidget, PathSolving_Form):
    addPathPoint = pyqtSignal(float, float)
    deletePathPoint = pyqtSignal(int)
    moveupPathPoint = pyqtSignal(int)
    movedownPathPoint = pyqtSignal(int)
    mergeResult = pyqtSignal(int)
    def __init__(self, FileState, data, resultData, width, parent=None):
        super(Path_Solving_show, self).__init__(parent)
        self.setupUi(self)
        self.FileState = FileState
        self.mechanism_data = resultData
        self.path = data
        for e in data: self.Point_list.addItem("({}, {})".format(e['x'], e['y']))
        for e in resultData: self.addResult(e)
        self.Point_list_Count()
        self.isGetResult()
    
    @pyqtSlot()
    def on_clearAll_clicked(self):
        self.Point_list.setCurrentRow(0)
        for i in reversed(range(self.Point_list.count()+1)): self.on_remove_clicked()
        self.Point_list_Count()
    
    @pyqtSlot()
    def on_series_clicked(self):
        dlg = Path_Solving_series_show()
        dlg.show()
        if dlg.exec_():
            for e in dlg.path: self.on_add_clicked(e[0], e[1])
    
    @pyqtSlot()
    def on_moveUp_clicked(self):
        n = self.Point_list.currentRow()
        if n>0 and self.Point_list.count()>1:
            self.moveupPathPoint.emit(n)
            x = self.Point_list.currentItem().text()[1:-1].split(', ')[0]
            y = self.Point_list.currentItem().text()[1:-1].split(', ')[1]
            self.Point_list.insertItem(n-1, '('+str(x)+", "+str(y)+')')
            self.Point_list.takeItem(n+1)
            self.Point_list.setCurrentRow(n-1)
    
    @pyqtSlot()
    def on_moveDown_clicked(self):
        n = self.Point_list.currentRow()
        if n<self.Point_list.count()-1 and self.Point_list.count()>1:
            self.movedownPathPoint.emit(n)
            x = self.Point_list.currentItem().text()[1:-1].split(', ')[0]
            y = self.Point_list.currentItem().text()[1:-1].split(', ')[1]
            self.Point_list.insertItem(n+2, '('+str(x)+", "+str(y)+')')
            self.Point_list.takeItem(n)
            self.Point_list.setCurrentRow(n+1)
    
    def addPath(self, x, y):
        self.Point_list.addItem('({}, {})'.format(x, y))
        self.Point_list_Count()
    
    @pyqtSlot()
    def on_add_clicked(self, x=False, y=False):
        if x is False:
            x = self.X_coordinate.value()
            y = self.Y_coordinate.value()
        self.addPathPoint.emit(x, y)
        self.Point_list.addItem("({}, {})".format(x, y))
        self.Point_list_Count()
    @pyqtSlot()
    def on_remove_clicked(self):
        if self.Point_list.currentRow()>-1:
            self.deletePathPoint.emit(self.Point_list.currentRow())
            self.Point_list.takeItem(self.Point_list.currentRow())
            self.Point_list_Count()
    
    def Point_list_Count(self):
        self.pointNum.setText(
            "<html><head/><body><p><span style=\" font-size:12pt; color:#00aa00;\">"+str(self.Point_list.count())+"</span></p></body></html>")
        self.Generate.setEnabled(self.Point_list.count()>1)
    
    @pyqtSlot()
    def on_Generate_clicked(self):
        type_num = 0 if self.type0.isChecked() else (1 if self.type1.isChecked() else 2)
        upper = [self.AxMax.value(), self.AyMax.value(), self.DxMax.value(), self.DyMax.value()]+[self.LMax.value()]*5
        lower = [self.AxMin.value(), self.AyMin.value(), self.DxMin.value(), self.DyMin.value()]+[self.LMin.value()]*5
        dlg = Path_Solving_progress_show(self.path, upper, lower, self.AMin.value(), self.AMax.value(),
            type_num, self.maxGen.value(), self.report.value()/100, self)
        dlg.show()
        if dlg.exec_():
            self.mechanism_data.append(dlg.mechanism)
            self.addResult(dlg.mechanism)
            sec = dlg.time_spand%60
            mins = int(dlg.time_spand/60)
            self.timeShow.setText("<html><head/><body><p><span style=\" font-size:10pt\">{} [min] {} [s]</span></p></body></html>".format(mins, sec))
            self.Tabs.setCurrentIndex(0)
            print('Finished.')
    
    def addResult(self, e):
        item = QListWidgetItem("{} ({} gen)".format(e['Algorithm'], e['maxGen']))
        item.setToolTip('\n'.join(['[{}]'.format(e['Algorithm'])]+[
            "{}: {}".format(k, v) for k, v in e.items() if not k in ['Algorithm', 'TimeAndFitness']]))
        self.Result_list.addItem(item)
    
    @pyqtSlot(int)
    def on_Result_list_currentRowChanged(self, cr): self.isGetResult()
    
    def isGetResult(self):
        n = self.Result_list.count()>0 and self.Result_list.currentRow()>-1
        self.mergeButton.setEnabled(n)
        self.deleteButton.setEnabled(n)
        self.copySettings.setEnabled(n)
    
    @pyqtSlot()
    def on_deleteButton_clicked(self):
        row = self.Result_list.currentRow()
        del self.mechanism_data[row]
        self.Result_list.takeItem(row)
        self.isGetResult()
    
    @pyqtSlot(QModelIndex)
    def on_Result_list_doubleClicked(self, index):
        row = self.Result_list.currentRow()
        if row!=-1: self.on_mergeButton_clicked()
    
    @pyqtSlot()
    def on_mergeButton_clicked(self):
        reply = QMessageBox.question(self, 'Prompt Message', "Merge this result to your canvas?",
            (QMessageBox.Apply | QMessageBox.Cancel), QMessageBox.Apply)
        if reply==QMessageBox.Apply: self.mergeResult.emit(self.Result_list.currentRow())
    
    @pyqtSlot()
    def on_getTimeAndFitness_clicked(self):
        results = [[e['Algorithm'], e['maxGen'], e['TimeAndFitness']] for e in self.mechanism_data]
        dlg = ChartDialog("Convergence Value", results, self)
        dlg.show()
    
    @pyqtSlot()
    def on_copySettings_clicked(self):
        args = self.mechanism_data[self.Result_list.currentRow()]
        if args['Algorithm']=='Genetic': self.type0.setChecked(True)
        elif args['Algorithm']=='Firefly': self.type1.setChecked(True)
        elif args['Algorithm']=="Differtial Evolution": self.type2.setChecked(True)
        self.isCustomize.setChecked(True)
        self.setArgs(maxGen=args['maxGen'], report=args['report'],
            AxMin=args['AxMin'], AyMin=args['AyMin'], DxMin=args['DxMin'], DyMin=args['DyMin'], LMin=args['LMin'], AMin=args['minAngle'],
            AxMax=args['AxMax'], AyMax=args['AyMax'], DxMax=args['DxMax'], DyMax=args['DyMax'], LMax=args['LMax'], AMax=args['maxAngle'])
        self.on_clearAll_clicked()
        for e in args['path']: self.on_add_clicked(e[0], e[1])
    
    @pyqtSlot()
    def on_isCustomize_clicked(self): self.setArgs()
    @pyqtSlot()
    def on_setDefault_clicked(self): self.setArgs()
    def setArgs(self, maxGen=1500, report=5, AxMin=-50., AyMin=-50., DxMin=-50., DyMin=-50., LMin=5., AMin=0.,
            AxMax=50., AyMax=50., DxMax=50., DyMax=50., LMax=50., AMax=360.):
        self.maxGen.setValue(maxGen)
        self.report.setValue(report)
        self.AxMin.setValue(AxMin)
        self.AyMin.setValue(AyMin)
        self.DxMin.setValue(DxMin)
        self.DyMin.setValue(DyMin)
        self.LMin.setValue(LMin)
        self.AMin.setValue(AMin)
        self.AxMax.setValue(AxMax)
        self.AyMax.setValue(AyMax)
        self.DxMax.setValue(DxMax)
        self.DyMax.setValue(DyMax)
        self.LMax.setValue(LMax)
        self.AMax.setValue(AMax)
