# conditional statment


"""
Logical Operators
Answer -> bool (True/False)

physics>33      chemistry>33
AND
Condition 1     Condition 2     Result
    F               F              F
    T               F              F
    F               T              F
    T               T              T

OR
Condition 1     Condition 2     Result
    F               F              F
    T               F              T
    F               T              T
    T               T              T

NOT

Reverses the result
"""
# physics = 22
# chemistry = 19

# print(physics > 33 and chemistry > 33)
# print(not (physics > 33 or chemistry > 33))
# print(physics > 33 and not chemistry > 33)
# False and True
# print(not physics > 22)


# age=int(input("enter your age:"))
# if age>=18:
#     print


n1 = int(input("enter num1: "))
n2 = int(input("enter num2: "))
if n1 > n2:
    print("n1 is greatest")
else:
    print("n2 is greatest")

{
	"String Input": {
		"prefix": "sinput",
		"body": [
			"${1:variableName} = input('${2:Enter a string}: ')",
			"$3"
		],
		"description": "Prompt user for a string input and assign it to a variable"
	},
	"Integer Input": {
		"prefix": "iinput",
		"body": [
			"${1:variableName} = int(input('${2:Enter an integer}: '))",
			"$3"
		],
		"description": "Prompt user for an integer input and assign it to a variable"
	}
}