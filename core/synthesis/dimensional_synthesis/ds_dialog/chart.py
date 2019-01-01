# -*- coding: utf-8 -*-

"""The chart dialog of dimensional synthesis result."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2019"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from core.QtModules import (
    QDialog,
    Qt,
    QSize,
    QVBoxLayout,
    QTabWidget,
    QCategoryAxis,
    QValueAxis,
    QLineSeries,
    QScatterSeries,
    QColor,
    QPointF,
    QWidget,
    QIcon,
    QChartView,
    QSizePolicy,
)
from core.graphics import DataChart


class ChartDialog(QDialog):

    """There are three charts are in the dialog.

    + Fitness / Generation Chart.
    + Generation / Time Chart.
    + Fitness / Time Chart.
    """

    def __init__(self, title, algorithm_data, parent: QWidget):
        """Add three tabs of chart."""
        super(ChartDialog, self).__init__(parent)
        self.setWindowTitle("Chart")
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)
        self.setSizeGripEnabled(True)
        self.setModal(True)
        self.setMinimumSize(QSize(800, 600))

        self.__title = title
        self.__algorithm_data = algorithm_data

        # Widgets
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(6, 6, 6, 6)
        self.tabWidget = QTabWidget(self)
        self.__set_chart("Fitness / Generation Chart", 0, 1)
        self.__set_chart("Generation / Time Chart", 2, 0)
        self.__set_chart("Fitness / Time Chart", 2, 1)
        main_layout.addWidget(self.tabWidget)

    def __set_chart(self, tab_name: str, pos_x: int, pos_y: int):
        """Setting charts by data index.

        pos_x / pos_y: [0], [1], [2]
        time_fitness: List[List[Tuple[gen, fitness, time]]]
        """
        axis_x = QCategoryAxis()
        axis_y = QValueAxis()
        axis_x.setLabelsPosition(QCategoryAxis.AxisLabelsPositionOnValue)
        axis_x.setMin(0)
        axis_y.setTickCount(11)

        if self.__algorithm_data:
            # Just copy references from algorithm data.
            plot = [data['time_fitness'] for data in self.__algorithm_data]

            # X max.
            max_x = int(max([max([tnf[pos_x] for tnf in data]) for data in plot]) * 100)
            axis_x.setMax(max_x)
            i10 = int(max_x / 10)
            if i10:
                for i in range(0, max_x + 1, i10):
                    axis_x.append(str(i / 100), i)
            else:
                for i in range(0, 1000, 100):
                    axis_x.append(str(i / 100), i)

            # Y max.
            max_y = max(max([tnf[pos_y] for tnf in data]) for data in plot) + 10
        else:
            plot = None
            # Y max.
            max_y = 100

        max_y -= max_y % 10
        axis_y.setRange(0., max_y)
        chart = DataChart(self.__title, axis_x, axis_y)

        # Append data set.
        for i, data in enumerate(self.__algorithm_data):
            line = QLineSeries()
            scatter = QScatterSeries()
            line.setName(f"{i}: {data['Algorithm']}")
            scatter.setMarkerSize(7)
            scatter.setColor(QColor(110, 190, 30))
            for i, e in enumerate(plot[self.__algorithm_data.index(data)]):
                y = e[pos_y]
                x = e[pos_x] * 100
                line.append(QPointF(x, y))
                scatter.append(QPointF(x, y))
            for series in (line, scatter):
                chart.addSeries(series)
                series.attachAxis(axis_x)
                series.attachAxis(axis_y)
            chart.legend().markers(scatter)[0].setVisible(False)
        # Add chart into tab widget
        widget = QWidget()
        self.tabWidget.addTab(widget, QIcon(), tab_name)
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(2, 2, 2, 2)
        chart_view = QChartView(chart)
        chart_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(chart_view)
