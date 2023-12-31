from functools import reduce

def get_row(text: str) -> int:
    return int(reduce(lambda acc, x: acc + ('0' if x == 'F' else '1'), text, ''), 2)

def get_col(text: str) -> int:
    return int(reduce(lambda acc, x: acc + ('0' if x == 'L' else '1'), text, ''), 2)

def get_seat_id(text: str) -> int:
    row_part = text[:7]
    col_part = text[7:]
    row = get_row(row_part)
    col = get_col(col_part)
    return 8 * row + col

result = reduce(max, map(get_seat_id, open('input2.txt').read().splitlines()))

print(result)