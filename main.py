from flask import Flask, render_template, redirect, url_for, flash, g, request, abort
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

alphabet = {"A": "*-", "B": "-***", "C": "-*-*", "D": "-**", "E": "*", "F": "**-*", "G": "--*", "H": "****", "I": "**",
            "J": "*---", "K": "-*-",
            "L": "*-**", "M": "--", "N": "-*", "O": "---", "P": "*--*", "Q": "--*-", "R": "*-*", "S": "***", "T": "-",
            "U": "**-", "V": "***-",
            "W": "*--", "X": "-**-", "Y": "-*--", "Z": "--**", "1": "*----", "2": "**---", "3": "***--", "4": "****-",
            "5": "*****", "6": "-****",
            "7": "--***", "8": "---**", "9": "----*", "0": "-----",
            ".": "*-*-*-", ",": "--**--", ":": "---***", "?": "**--**", "'": "*----*", "-": "-****-", '"': "*-**-*"}

key_list = list(alphabet.keys())
val_list = list(alphabet.values())

app = Flask(__name__)
app.config['SECRET_KEY'] = "lkdsaujdio23981321"
Bootstrap(app)


class Converter(FlaskForm):
    to_convert = StringField("Enter your text or your code morse here", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/", methods=['POST', 'GET'])
def home():
    form = Converter()
    string = "Your code morse or your text will appear here!"
    if form.validate_on_submit():
        text = request.form.get("to_convert").upper()
        if "*" not in text.split():
            encoded_message = []
            for i in text:
                if i == " ":
                    encoded_message.append("/ ")
                else:
                    encoded_message.append(f"{alphabet[i]} ")
            string = ''.join([str(item) for item in encoded_message])
            return render_template("index.html", text=string, form=form)
        elif "*" or "-" in text.split():
            decoded_message = []
            for i in text.split():
                if i == "/":
                    decoded_message.append(" ")
                else:
                    decoded_message.append(key_list[val_list.index(i)])
            string = ''.join([str(item) for item in decoded_message])
            return render_template("index.html", text=string, form=form)
    return render_template("index.html", form=form, text=string)


# print(f"Welcome to the Text to Morse Code Converter")
# # code_on = True
# # while code_on:
# #     choice = input("What would you like to do? Type 1 to convert text to morse or "
# #                    f"type 2 to convert morse to text: ")
# #
# #     if choice == "1":
# #         print("You've chosen to convert text to morse.")
# #         text = input("Type the text that you would like to convert: ").upper()
#         encoded_message = []
#         for i in text:
#             if i == " ":
#                 encoded_message.append("/ ")
#             else:
#                 encoded_message.append(f"{alphabet[i]} ")
#         string =''.join([str(item) for item in encoded_message])
# #         print(f"Your encoded text is: {string}")
# #         final = input("Would you like to use the converter again? Type Yes or No: ").lower()
# #         if final == "no":
# #             code_on = False
# #
# #     elif choice == "2":
# #         print("You've chosen to convert morse to text.")
# #         text = input("Type the code that you would like to decode: ").split()
# #         decoded_message = []
# #         for i in text:
# #             if i == "/":
# #                 decoded_message.append(" ")
# #             else:
# #                 decoded_message.append(key_list[val_list.index(i)])
# #         string = ''.join([str(item) for item in decoded_message])
# #         print(f"Your decoded text is: {string}")
# #     else:
# #         print("Please type a correct option.")
# #

if __name__ == "__main__":
    app.run(debug=True)
