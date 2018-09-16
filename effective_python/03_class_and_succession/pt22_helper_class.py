# vim: set fileencoding=utf-8 :
"""
項目22: 辞書やタプルで記録管理するよりもヘルパークラスを使う
"""


class SimpleGradebook(object):

    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].apppend(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)
