'''
QR Decoder
Given a 6x6 matrix (array of arrays), representing a QR code, return the string of binary data in the code.

The QR code may be given in any rotation of 90 degree increments.
A correctly oriented code has a 2x2 group of 1's (orientation markers) in the bottom-left, top-left, and top-right corners.
The three 2x2 orientation markers are not part of the binary data.
The binary data is read left-to-right, top-to-bottom (like a book) when the QR code is correctly oriented.
A code will always have exactly one valid orientation.
For example, given:

[
  "110011",
  "110011",
  "000000",
  "000000",
  "110000",
  "110001"
]
or given the same code with a different orientation:

[
  "110011",
  "110011",
  "000000",
  "000000",
  "000011",
  "100011"
]
Return "000000000000000000000001", all the binary data excluding the three 2x2 orientation markers.
'''


def decode_qr(qr_code):
    grid = [list(row) for row in qr_code]

    # print(grid)

    def rotate_90(m):
        n = len(m)
        return [[m[n - 1 - j][i] for j in range(n)] for i in range(n)]

    def is_correct(m):
        if not (m[0][0] == m[0][1] == m[1][0] == m[1][1] == "1"):
            return False
        if not (m[0][4] == m[0][5] == m[1][4] == m[1][5] == "1"):
            return False
        if not (m[4][0] == m[4][1] == m[5][0] == m[5][1] == "1"):
            return False
        return True

    current = grid
    print(current)

    for _ in range(4):
        if is_correct(current):
            break
        current = rotate_90(current)



    data_bits = []
    for i in range(6):
        for j in range(6):
            if i < 2 and j < 2:
                continue
            if i < 2 and j >= 4:
                continue
            if i >= 4 and j < 2:
                continue
            data_bits.append(current[i][j])
    result = ''.join(data_bits)
    print(result)
    qr_code = result
    return qr_code


# t = decode_qr(["110011", "110011", "000000", "000000", "110000", "110001"])
# print(t)

t1 = decode_qr(["100011", "000011", "000000", "000000", "110011", "110011"])
print(t1)