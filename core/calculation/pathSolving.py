# -*- coding: utf-8 -*-
##Pyslvs - Open Source Planar Linkage Mechanism Simulation and Dimensional Synthesis System.
##Copyright (C) 2016-2017 Yuan Chang
##E-mail: pyslvs@gmail.com
##
##This program is free software; you can redistribute it and/or modify
##it under the terms of the GNU Affero General Public License as published by
##the Free Software Foundation; either version 3 of the License, or
##(at your option) any later version.
##
##This program is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Affero General Public License for more details.
##
##You should have received a copy of the GNU Affero General Public License
##along with this program; if not, write to the Free Software
##Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

from ..QtModules import *
import timeit, numpy
from ..kernel.pyslvs_generate import tinycadlib
from ..kernel.pyslvs_generate.planarlinkage import build_planar

class WorkerThread(QThread):
    done = pyqtSignal(dict, int)
    def __init__(self, type_num, mechanismParams, GenerateData, algorithmPrams, parent=None):
        super(WorkerThread, self).__init__(parent)
        self.stoped = False
        self.mutex = QMutex()
        self.type_num = type_num
        self.mechanismParams = mechanismParams
        self.GenerateData = GenerateData
        self.algorithmPrams = algorithmPrams
        self.socket = None
    def setSocket(self, socket): self.socket = socket
    
    def run(self):
        with QMutexLocker(self.mutex): self.stoped = False
        print("Algorithm: {}".format("Genetic Algorithm" if self.type_num==0 else "Firefly Algorithm" if self.type_num==1 else "Differtial Evolution"))
        print("Through: {}".format(self.mechanismParams['targetPath']))
        t0 = timeit.default_timer()
        TnF, FP = self.generateProcess()
        t1 = timeit.default_timer()
        time_spand = round(t1-t0, 2)
        mechanism = {
            'Algorithm':'RGA' if self.type_num==0 else 'Firefly' if self.type_num==1 else 'DE',
            'time':time_spand,
            'Ax':FP[0], 'Ay':FP[1],
            'Dx':FP[2], 'Dy':FP[3],
            'mechanismParams':self.mechanismParams,
            'GenerateData':self.GenerateData,
            'algorithmPrams':self.algorithmPrams,
            'TimeAndFitness':TnF}
        for i in range(len(self.mechanismParams['Link'].split(','))): mechanism['L{}'.format(i)] = FP[4+i]
        print('total cost time: {} [s]'.format(time_spand))
        self.done.emit(mechanism, time_spand)
    
    #TODO: Put socket into Cython lib.
    def generateProcess(self):
        if not self.socket==None:
            from ..server.rga import Genetic
            from ..server.firefly import Firefly
            from ..server.de import DiffertialEvolution
        else:
            from ..kernel.pyslvs_generate.rga import Genetic
            from ..kernel.pyslvs_generate.firefly import Firefly
            from ..kernel.pyslvs_generate.de import DiffertialEvolution
        mechanismObj = build_planar(self.mechanismParams)
        #Genetic Algorithm
        if self.type_num==0:
            APs = {
                'nParm':self.GenerateData['nParm'],
                'nPop':self.algorithmPrams['nPop'], #250
                'pCross':self.algorithmPrams['pCross'], #0.95
                'pMute':self.algorithmPrams['pMute'], #0.05
                'pWin':self.algorithmPrams['pWin'], #0.95
                'bDelta':self.algorithmPrams['bDelta'], #5.
                'upper':self.GenerateData['upper'],
                'lower':self.GenerateData['lower'],
                'maxGen':self.GenerateData['maxGen'],
                'report':self.GenerateData['report']}
            if not self.socket==None:
                APs['socket_port'] = self.socket
                APs['targetPath'] = self.mechanismParams['targetPath']
            self.foo = Genetic(mechanismObj, **APs)
        #Firefly Algorithm
        elif self.type_num==1:
            APs = {
                'D':self.GenerateData['nParm'],
                'n':self.algorithmPrams['n'], #40
                'alpha':self.algorithmPrams['alpha'], #0.01
                'betaMin':self.algorithmPrams['betaMin'], #0.2
                'gamma':self.algorithmPrams['gamma'], #1.
                'beta0':self.algorithmPrams['beta0'], #1.
                'ub':self.GenerateData['upper'],
                'lb':self.GenerateData['lower'],
                'maxGen':self.GenerateData['maxGen'],
                'report':self.GenerateData['report']}
            if not self.socket==None:
                APs['socket_port'] = self.socket
                APs['targetPath'] = self.mechanismParams['targetPath']
            self.foo = Firefly(mechanismObj, **APs)
        #Differential Evolution
        elif self.type_num==2:
            APs = {
                'D':self.GenerateData['nParm'],
                'strategy':self.algorithmPrams['strategy'], #1
                'NP':self.algorithmPrams['NP'], #190
                'F':self.algorithmPrams['F'], #0.6
                'CR':self.algorithmPrams['CR'], #0.9
                'upper':self.GenerateData['upper'],
                'lower':self.GenerateData['lower'],
                'maxGen':self.GenerateData['maxGen'],
                'report':self.GenerateData['report']}
            if not self.socket==None:
                APs['socket_port'] = self.socket
                APs['targetPath'] = self.mechanismParams['targetPath']
            self.foo = DiffertialEvolution(mechanismObj, **APs)
        time_and_fitness, fitnessParameter = self.foo.run()
        return(tuple(tuple(float(v) for v in e.split(',')) for e in time_and_fitness.split(';')[0:-1]),
            [float(e) for e in fitnessParameter.split(',')])
    
    def stop(self):
        with QMutexLocker(self.mutex): self.stoped = True
