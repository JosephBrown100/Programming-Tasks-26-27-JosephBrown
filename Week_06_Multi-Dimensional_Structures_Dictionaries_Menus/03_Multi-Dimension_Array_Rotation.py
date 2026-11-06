"""
TASK: 03 Multi-Dimension Array Rotation

# Rotate a 2D matrix 90 degrees clockwise manually
Good luck

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random as r

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass



def rotate_matrix(matrix):
    n = len(matrix)

    for e in matrix:
        print(e)
    
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            for g in matrix:
                print(g)
            print("\n")
    
    for i in range(n):
        matrix[i].reverse()
    return matrix 




if __name__ == "__main__":
    main()
    matrix=[[7,8,9],
            [4,5,6],
            [1,2,3]]
    matrix = rotate_matrix(matrix)
    for i in matrix:
        print(i)