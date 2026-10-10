N = 8

def solve(board, row):
    if row == N:
        return True

    for col in range(N):
        safe = True

        for i in range(row):
            if (board[i] == col or
                abs(board[i] - col) == abs(i - row)):
                safe = False
                break

        if safe:
            board[row] = col

            if solve(board, row + 1):
                return True

    return False

board = [-1] * N

if solve(board, 0):
    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution")
