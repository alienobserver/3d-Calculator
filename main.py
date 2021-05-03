# 3d Calculator App
# to install pyqt5 run $ pip install pyqt5

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication
import sys
import os
import calcGUI
from funcs3d import *


# The main class
class Calculator3d(QtWidgets.QMainWindow, calcGUI.Ui_Calculator3d):
    def __init__(self, parent=None):
        super(Calculator3d, self).__init__(parent)
        # Filepath where are located our images
        self.file = (os.path.abspath(os.path.dirname(sys.argv[0])) + "/3dcalcImages/").replace("\\", "/")

        self.setupUi(self)

        # Setup all on click functions for buttons and image showing buttons
        self.TriangleButton.clicked.connect(self.TriangleImage)
        self.TriangleS.clicked.connect(self.AreaOfTriangle)
        self.TriangleP.clicked.connect(self.PerimeterOfTriangle)

        self.SquareButton.clicked.connect(self.SquareImage)
        self.SquareS.clicked.connect(self.AreaOfSquare)
        self.SquareP.clicked.connect(self.PerimeterOfSquare)

        self.RectangleButton.clicked.connect(self.RectImage)
        self.RectangleS.clicked.connect(self.AreaOfRect)
        self.RectangleP.clicked.connect(self.PerimeterOfRect)

        self.CircleButton.clicked.connect(self.CircleImage)
        self.CircleS.clicked.connect(self.AreaOfCircle)
        self.CircleC.clicked.connect(self.CircumferenceOfCircle)

        self.TriangularPrismButton.clicked.connect(self.TriangularPrismImage)
        self.TriangularPrismV.clicked.connect(self.VolumeOfTriangularPrism)

        self.CubeButton.clicked.connect(self.CubeImage)
        self.CubeV.clicked.connect(self.VolumeOfCube)

        self.RectangularCubeButton.clicked.connect(self.RectCubeImage)
        self.RectangularCubeV.clicked.connect(self.VolumeOfRectCube)

        self.SphereButton.clicked.connect(self.SphereImage)
        self.SphereV.clicked.connect(self.VolumeOfSphere)

    # function for making on click functions
    def OnClick(self, buttonFunc, *textInputs):
        try:
            textInputs = [int(i.text()) for i in textInputs]
            self.label.setText(str(buttonFunc(textInputs)))
        except:
            self.label.setText("Please Enter the needed fields")

    # functions for 3d calculations and for changing the label
    def AreaOfTriangle(self, qmodelindex):
        # Try to get all integer variables from our text inputs for triangle else set them to None
        try:
            a = int(self.TriangleA.text())
        except:
            a = None
        try:
            b = int(self.TriangleB.text())
        except:
            b = None
        try:
            c = int(self.TriangleC.text())
        except:
            c = None
        try:
            angleA = int(self.TriangleAngleA.text())
        except:
            angleA = None
        try:
            angleB = int(self.TriangleAngleB.text())
        except:
            angleB = None
        try:
            angleC = int(self.TriangleAngleC.text())
        except:
            angleC = None
        try:
            heightA = int(self.TriangleHeightA.text())
        except:
            heightA = None
        try:
            heightB = int(self.TriangleHeightB.text())
        except:
            heightB = None
        try:
            heightC = int(self.TriangleHeightC.text())
        except:
            heightC = None
        try:
            self.label.setText(
                str(AreaOfTriangle([a, b, c, angleA, angleB, angleC, heightA, heightB, heightC])))
        except:
            self.label.setText("Please Enter the needed fields")

    def PerimeterOfTriangle(self, qmodelindex):
        self.OnClick(PerimeterOfTriangle, self.TriangleA, self.TriangleB, self.TriangleC)

    def AreaOfSquare(self, qmodelindex):
        self.OnClick(AreaOfSquare, self.SquareA)

    def PerimeterOfSquare(self, qmodelindex):
        self.OnClick(PerimeterOfSquare, self.SquareA)

    def AreaOfRect(self, qmodelindex):
        self.OnClick(AreaOfRect, self.RectangleA, self.RectangleB)

    def PerimeterOfRect(self, qmodelindex):
        self.OnClick(PerimeterOfRect, self.RectangleA, self.RectangleB)

    def AreaOfCircle(self, qmodelindex):
        self.OnClick(AreaOfCircle, self.CircleR)

    def CircumferenceOfCircle(self, qmodelindex):
        self.OnClick(CircumferenceOfCircle, self.CircleR)

    def VolumeOfTriangularPrism(self, qmodelindex):
        self.OnClick(VolumeOfTriangularPrism, self.TriangularPrismA, self.TriangularPrismB, self.TriangularPrismC, self.TriangularPrismH)

    def VolumeOfCube(self, qmodelindex):
        self.OnClick(VolumeOfCube, self.CubeA)

    def VolumeOfRectCube(self, qmodelindex):
        self.OnClick(VolumeOfRectCube, self.RectangularCubeA, self.RectangularCubeB, self.RectangularCubeC)

    def VolumeOfSphere(self, qmodelindex):
        self.OnClick(VolumeOfSphere, self.SphereR)   


    # function for setting no-repeated background image for widget
    def background(self, img_name):
        self.ImageWidget.setStyleSheet(("background-image: url(%s); background-repeat: no-repeat;" % (self.file + img_name)))

    # functions for every image showing buttons
    def TriangleImage(self, qmodelindex):
        self.background("Triangle.png")

    def SquareImage(self, qmodelindex):
        self.background("Square.png")

    def RectImage(self, qmodelindex):
        self.background("Rectangle.png")

    def CircleImage(self, qmodelindex):
       self.background("Circle.png")

    def TriangularPrismImage(self, qmodelindex):
        self.background("TriangularPrism.png")

    def CubeImage(self, qmodelindex):
        self.background("Cube.png")

    def RectCubeImage(self, qmodelindex):
        self.background("RectangularCube.png")

    def SphereImage(self, qmodelindex):
        self.background("Sphere.png")

# The main function which runs app
def main():
    app = QApplication(sys.argv)
    form = Calculator3d()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
