def get_row(rowIndex):
    row = [1]
    for _ in range(rowIndex):
        row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]
    return row


rowIndex = int(input())
print(get_row(rowIndex))
