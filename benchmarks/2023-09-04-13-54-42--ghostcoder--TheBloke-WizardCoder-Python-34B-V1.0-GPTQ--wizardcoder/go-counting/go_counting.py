
import sys
sys.setrecursionlimit(2500)

def main():
    board = [["B", ".", "W"], ["W", "W", "."], ["W", ".", "."]]
    b = Board(board)
    print(b.territories())

if __name__ == "__main__":
    main()