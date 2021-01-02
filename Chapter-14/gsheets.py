import ezsheets

ss=ezsheets.Spreadsheet('https://docs.google.com/spreadsheets/d/1CAByXK20ko5zoVHQjnzOxsyIlFSzHBMROCtQANPfIuQ/edit#gid=311668401')
sheet=ss[0]

mail=sheet.getColumn(3)
bl=mail.index('')
mail=mail[1:bl]
print(mail)