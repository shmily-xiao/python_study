#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import time
import xlwt

def read_xls(path):

    xlsfile = path  # 打开指定路径中的xls文件

    book = xlrd.open_workbook(xlsfile)  # 得到Excel文件的book对象，实例化对象

    sheet_name = book.sheet_names()[0]  # 获得指定索引的sheet表名字
    # print "2、", sheet_name
    return book.sheet_by_name(sheet_name)  # 通过sheet名字来获取，当然如果知道sheet名字就可以直接指定

def write_excel(path, data, col_name, data_time):
    # Create a workbook and add a worksheet.
    workbook = xlwt.Workbook('utf-8')
    worksheet = workbook.add_sheet("平均")

    col = 2
    for name in col_name:
        worksheet.write(0, col, name)
        col += 1

    # Start from the first cell. Rows and columns are zero indexed.
    row = 1 # 行

    # Iterate over the data and write it out row by row.
    for address, value in data.items():
        col = 0
        worksheet.write(row, col, address)
        for my_time in data_time:
            avgs = value.get(my_time)
        # for my_time, avgs in value.items():
            col = 1
            worksheet.write(row, col, my_time)
            for avg in avgs:
                worksheet.write(row, col+1, avg)
                col += 1
            row += 1

    # Write a total using a formula.
    # worksheet.write(row, 0, 'Total')
    # worksheet.write(row, 1, '=SUM(B1:B4)')

    workbook.save("text.xls")


def avg_handler(sheet):
    nrows = sheet.nrows  # 获取行总数
    ncols = sheet.ncols  # 获取列总数

    flag = 0 # 23 开始计算平均值
    sum_count = 0.0 # 为了计算23个小时个数
    col_name = []
    result = {}
    data_time=[]

    pre_address_name = ""
    for col in xrange(ncols - 2):
        col_name.append(sheet.cell_value(0,col+2))
        my_need_time = ""
        for row in xrange(nrows):
            if row == 0: continue
            point_name = sheet.cell_value(row,0)

            create_time = time.strptime(sheet.cell_value(row,1), "%Y-%m-%d %H:%M")
            create_time_hour = create_time.tm_hour
            if create_time_hour == 11:
                my_need_time = sheet.cell_value(row, 1)[0:10]
                pre_address_name = point_name

            if create_time_hour != 10:
                flag = flag + 1

            if flag != 23 or create_time_hour == 9:
                # 如果跨地域了且没有满足22个也需要被重置
                if point_name != pre_address_name:
                    flag = 0
                    sum_count = 0.0
                    continue
                # 如果没有到23个数据就到了10点就需要去掉这一部分数据
                if create_time_hour == 10:
                    flag = 0
                    sum_count = 0.0
                    continue
                # print row
                # print  2 + col
                # print sheet.cell_value(row, 2 + col)
                if sheet.cell_value(row, 2 + col):
                    value = sheet.cell_value(row, 2 + col)
                else:
                    value = 0.0
                sum_count = sum_count + value
                continue

            sum_avg = round(sum_count / 23.0,2)
            if point_name not in result:
                result[point_name] = {my_need_time:[sum_avg]}
            else:
                if my_need_time not in result[point_name]:
                    result[point_name][my_need_time]=[sum_avg]
                else:
                    result[point_name][my_need_time].append(sum_avg)
            # 统计完了之后需要将数据清零
            flag = 0
            sum_count = 0.0
            pre_address_name=point_name
            if my_need_time not in data_time:
                data_time.append(my_need_time)

    return result, col_name, data_time


if __name__ == '__main__':
    path = "xxx.xls"
    sheet = read_xls(path)
    res,col_name, data_time = avg_handler(sheet)
    write_excel("",res, col_name, data_time)

    pass