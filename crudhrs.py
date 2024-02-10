import os
import pandas as pd
from openpyxl import load_workbook, Workbook
import xlrd


class Sistema:

    def __init__(self) -> None:
        pass

    def origina(self):
        
        pass
        book = pd.read_excel('UNIDADE.xlsx', sheet_name='unidade')
        book_dic = book.to_dict('list')



        return book_dic
