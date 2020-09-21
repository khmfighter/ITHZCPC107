'''
Excel表格操作
'''

import xlwt,xlrd

def write_xls():
    #1.创建workbook对象
    workbook=xlwt.Workbook()
    #2.创建sheet
    first_sheet=workbook.add_sheet("销售表")
    #3.（1）行索引   （2）列索引  （3）数据
    first_sheet.write(0, 0, "id")
    first_sheet.write(0, 1, "name")
    first_sheet.write(0, 2, "age")
    first_sheet.write(0, 3, "sex")

    #写数据
    for i in range(1,10):
        first_sheet.write(i, 0, 1000+i)
        first_sheet.write(i, 1, "xiaoming"+str(i))
        first_sheet.write(i, 2, 18)
        first_sheet.write(i, 3, "男")
    #5.保存数据
    workbook.save("测试数据.xls")
# write_xls()

def read_xls():
    #1.获取workbook对象
    workbook=xlrd.open_workbook("测试数据.xls")
    #2.获取sheet表
    sheet=workbook.sheet_by_name("销售表")
    #3.读取内容
    row_count=sheet.nrows
    col_count=sheet.ncols
    print(row_count,"行",col_count,"列")
    for i in range(row_count):
        for j in range(col_count):
            print(sheet.row_values(i)[j],end=" ")
        print()

read_xls()
