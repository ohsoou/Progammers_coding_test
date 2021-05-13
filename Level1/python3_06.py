#크레인 인형뽑기 게임 
def solution(board, moves):
    answer = 0
    basket = [];
    top = -1;
    for j in moves:
        for i in range(len(board)):
            if (board[i][j-1] != 0):
                current = board[i][j-1]

                board[i][j-1] = 0
                top += 1
                basket.append(current)

                if (top > 0 and basket[top] == basket[top-1]):
                    del basket[top]
                    del basket[top-1]
                    top -= 2
                    answer += 2
                break


    return answer
