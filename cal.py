
# num1 = int(input("Enter the first number: "))
# operator = input("Enter the operator (+, -, *, /): ")
# num2 = int(input("Enter the second number: "))
# if operator == "+":
#     result = num1 + num2
#     print("The result is: ", result)
# elif operator == "-":
#     result = num1 - num2
#     print("The result is: ", result)
# elif operator == "*":
#     result = num1 * num2
#     print("the result is: ", result)
# elif operator == "/":
#     if num2 !=0:
#         result = num1 // num2
#         print("The result is: ", result)
#     else:
#         print("Operation cannot be performed. Division by Zero is not allowed.")
# else:
#     print("Invalid operator. Please enter a valid operator.")


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def calculator():
    result = None

    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        operator = request.form["operator"]

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Division by zero not allowed"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)