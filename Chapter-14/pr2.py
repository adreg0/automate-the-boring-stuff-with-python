import ezsheets
ss=ezsheets.upload('example.xlsx')
ss.downloadAsODS()
ss.downloadAsExcel()
ss.downloadAsPDF()
ss.downloadAsCSV()