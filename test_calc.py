import pytest
from PyQt5.QtWidgets import QApplication
from calculator import Calculator

def test_addition():
    app = QApplication([])
    calc = Calculator()
    calc.display.setText('2+2')
    calc.buttonClicked('=')
    assert calc.display.text() == '4'
    app.exit()

def test_subtraction():
    app = QApplication([])
    calc = Calculator()
    calc.display.setText('10-5')
    calc.buttonClicked('=')
    assert calc.display.text() == '5'
    app.exit()

def test_multiplication():
    app = QApplication([])
    calc = Calculator()
    calc.display.setText('3*4')
    calc.buttonClicked('=')
    assert calc.display.text() == '12'
    app.exit()

def test_division():
    app = QApplication([])
    calc = Calculator()
    calc.display.setText('10/2')
    calc.buttonClicked('=')
    assert calc.display.text() == '5.0'
    app.exit()

def test_division_by_zero():
    app = QApplication([])
    calc = Calculator()
    calc.display.setText('5/0')
    calc.buttonClicked('=')
    assert calc.display.text() == 'Error'
    app.exit()

def test_clear_display():
    app = QApplication([])
    calc = Calculator()
    calc.display.setText('3+4')
    calc.buttonClicked('C')
    assert calc.display.text() == ''
    app.exit()

def test_history_save():
    app = QApplication([])
    calc = Calculator()
    calc.display.setText('3+4')
    calc.buttonClicked('=')
    assert calc.history.item(calc.history.count() - 1).text() == '3+4 = 7'

