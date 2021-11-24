from decimal import *
getcontext().prec = 20
import xlwt
from xlwt import Workbook

wb = Workbook()
cSheet = wb.add_sheet('testing')
decimal_style = xlwt.XFStyle()
decimal_style.num_format_str = '0.00000000000000000000'

thing = '0.000000358949654076'
thingie= Decimal(thing)
cSheet.write(0, 0, thingie, decimal_style)

wb.save('testing.xlsx')
