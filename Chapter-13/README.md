1) It returns a workbook.
2) wb.sheetnames contain worksheet object.
3) wb['Sheet1']
4) wb.active
5) sheet.cell(row=5,column=3).value
6) sheet.cell(row=5,colun=3).value='hello'
7) cell.row,cell.column
8) They hold the values of highest row and column.
9) openpyxl.cell.column_index_from_string('M')
10) openpyxl.cell.get_column_letter(14)

11) sheet ['A1':'F1']
12) wb.save('example.xslx')
13) By setting the cell value to a string of formula with a prefix =
14) .
15) sheet.row_dimensions[5].height = 100
16)  sheet.column_dimensions['C'].hidden = True
17) freeze panes are used for headers. They are always displayed irrespective of page.
18) 
    
* add_chart()
* openpyxl.charts.Series()
* openpyxl.charts.Reference()
* chartObj.append(seriesObj)
* openpyxl.charts.BarChart()
