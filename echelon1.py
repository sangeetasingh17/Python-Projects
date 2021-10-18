
# multiply a list by a number
def mul(row, num):
    return [x * num for x in row]

# subtract one row from another


def sub(row_left, row_right):
    return [a - b for (a, b) in zip(row_left, row_right)]

# calculate the row echelon form of the matrix


def echelonify(rw, i, m):
    for j, row in enumerate(m[(i+1):]):
        j += 1
        # print("rw[i]:", rw[i])
        if rw[i] != 0:
            m[j+i] = sub(row, mul(rw, row[i] / rw[i]))
    return rw


def row_echelon(m):
    for i in range(len(m)):  # len(m) == m x n
        active_row = m[i]
        echelonify(active_row, i, m)

    # close to zero
    m = [[(0 if (0.0000000001 > x > -0.0000000001) else x)
          for x in row]for row in m]

    return m


if __name__ == '__main__':
    print("Enter number of rows and columns")
    m, n = map(int, input().split())  # m = row and n = column
    M = []
    for _ in range(m):
        row = list(map(int, input().split()))[:n]
        M.append(row)

    mat = row_echelon(M)
    for row in mat:
        print(' '.join((str(x) for x in row)))

# The output can be printed by dividing each element of each row by the first non-zero element of the respective row in order to get 1
