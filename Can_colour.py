def can_color(matrix):
    
    #changing the given matrix to a matrix through which i can process.
    req_matrix = []
    for i in range(len(matrix)):
        temp_list = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                temp_list.append(j)
        req_matrix.append(temp_list)

    red_blue = {}
    stack = []
    #iterating over the required matrix.
    for i in range(len(req_matrix)):
        if i not in red_blue:
            #putting the node in stack
            stack=[i]
            #assigning it a colour Blue
            red_blue[i] = 0 
            while stack :
                element = stack.pop()
                for j in req_matrix[element]:
                    if j not in red_blue:
                        stack.append(j)
                        #Giving its adjacent nodes different colour i.e Red.
                        red_blue[j] = red_blue[element] ^ 1
                    #if bot are having same colour the returning false as Alice cannot colour the graph
                    elif red_blue[j] == red_blue[element]:
                        return False
    return True