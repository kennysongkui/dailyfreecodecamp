'''
Par for the Hole
Given two integers, the par for a golf hole and the number of strokes a golfer took on that hole, return the golfer's score using golf terms.

Return:

"Hole in one!" if it took one stroke.
"Eagle" if it took two strokes less than par.
"Birdie" if it took one stroke less than par.
"Par" if it took the same number of strokes as par.
"Bogey" if it took one stroke more than par.
"Double bogey" if took two strokes more than par.
'''

def golf_score(par, strokes):

    result = None

    if strokes == 1 :
        result = "Hole in one!"
        return result

    result_dic = {
        -2: "Eagle",
        -1: "Birdie",
        0: "Par",
        1:"Bogey",
        2:"Double bogey"
    }
    test = strokes - par
    # print(type(test))
    result = result_dic[test]
    # print(result_dic["-2"])
    par = result

    return par

# t = golf_score(3, 3)
# print(t)

t1 = golf_score(4, 3)
print(t1)