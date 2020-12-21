import xlrd
def ReadExcel(sheet,filename=None):
    if not filename:
        filename="../data/data.xlsx"
        data=xlrd.open_workbook(filename)
        tanle=data.sheet_by_name(sheet)
        return tanle.row_values(1)
