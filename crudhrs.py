import os
from flask import request
import pandas as pd
from openpyxl import load_workbook, Workbook
import xlrd


class Sistema:

    def __init__(self, sourc):
        self.sourc = 'UNIDADE.xlsx'

    def origina(self):
        
        pass
        book = pd.read_excel(self.sourc, sheet_name='unidade')
        book_dic = book.to_dict('list')



        return book_dic

    def addciona(self):
        
        book_to_add = load_workbook(self.sourc)

