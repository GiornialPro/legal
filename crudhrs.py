import os
from flask import request
import pandas as pd
from openpyxl import load_workbook, Workbook
import xlrd


class Sistema:

    def __init__(self, sourc):
        self.sourc = sourc

    def origina(self):
        
        pass
        book = pd.read_excel(self.sourc, sheet_name='unidade')
        book_dic = book.to_dict('list')

        return book_dic

    def addciona(self):
        
        book_to_add = load_workbook(self.sourc)

        if request.method == 'POST':

            user = request.form['user']
            senha = request.form['senha']
            magic = request.form['magicword']

            if f'{magic}'.strip() == 'registrar':
                pass
                
                book_to_add.create_sheet('usuarios')

                book_to_add['usuarios'][xlrd.cellname( 0, 0 )] = 'Nome'
                book_to_add['usuarios'][xlrd.cellname( 0, 1 )] = 'chave'

                book_to_add.save(self.sourc)
