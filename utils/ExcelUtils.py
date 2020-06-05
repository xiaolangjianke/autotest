# coding=utf-8
import xlrd
from xlutils.copy import copy
import os

from config.config import FILE_DIR

''' 对excel文件的处理'''


class ExcelUtils:

    def __init__(self, excel_path=None, index=None):
        defaul_path = FILE_DIR + '/data.xlsx'
        if excel_path == None:
            self.excel_path = defaul_path
        else:
            self.excel_path = excel_path
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheet_by_name(index)

    # 获取excel数据，按照每行一个list，添加到一个大的list里面
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(1, rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    # 获取Excel的行数
    def get_lines(self):
        # 行数
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    # 获取单元格的数据
    def get_col_value(self, row, col):
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        return None

    # 写入数据
    def write_value(self, row, value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save(self.excel_path)


if __name__ == '__main__':
    ex = ExcelUtils(index="Sheet1")
    data = ex.get_data()
    print(data)
