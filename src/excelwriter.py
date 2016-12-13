import xlsxwriter


def write(file_path):
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0
    worksheet.write(row, col, "Phone")
    worksheet.write(row, col + 1, "Name")
    worksheet.write(row, col + 2, "Create")
    row += 1
    for phone, name, created in channel_users:
        worksheet.write(row, col, phone)
        worksheet.write(row, col + 1, name.decode('utf8'))
        worksheet.write(row, col + 2, created.strftime('%Y-%m-%d %H:%M:%S'))
        row += 1

    workbook.close()