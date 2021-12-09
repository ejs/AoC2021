bingo_data = open("input_4").readlines()

calls = [int(c) for c in bingo_data[0].split(",")]
print(calls)

def parse_board(board):
    return [[int(c) for c in l.split()] for l in board]


def won(board, drawn):
    size = len(board[0])
    for x in range(size):
        if all(board[x][y] in drawn for y in range(size)):
            return True
        if all(board[y][x] in drawn for y in range(size)):
            return True
    if all(board[i][i] in drawn for i in range(size)):
        return True
    if all(board[i][size-i-1] in drawn for i in range(size)):
        return True
    return False


current = []
boards = []
for l in bingo_data[1:]:
    if l == "\n":
        if current:
            boards.append(parse_board(current))
        current = []
    else:
        current.append(l.strip())

called = set()
for c in calls:
    called.add(c)
    for board in boards:
        if won(board, called):
            print(c * sum(i for row in board for i in row if i not in called))
            break
    else:
        continue
    break

live = boards[:]
called = set()
for c in calls:
    called.add(c)
    live = [b for b in live if not won(b, called)]
    if len(live) == 1:
        last = live[0]
        break

print(last)
called = set()
for c in calls:
    called.add(c)
    if won(last, called):
        print(c, called)
        print(c * sum(i for row in last for i in row if i not in called))
        break
