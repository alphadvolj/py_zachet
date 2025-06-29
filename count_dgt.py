def count_dgt(number: int) -> dict:
    counts = {str(d): 0 for d in range(10)}
    for digit in str(number):
        counts[digit] += 1
    return counts


n = int(input())
result = count_dgt(n)
for d in range(10):
    print(f"{d}: {result[str(d)]}")
