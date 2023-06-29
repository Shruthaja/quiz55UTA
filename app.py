import re

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == "POST":
        l1=request.form["l1"]
        l2=request.form["l2"]
        iv=request.form["notallowed"]
        f=open("conditions.txt","w",encoding='utf8')
        f.write(l1+" "+l2+" "+iv)
        f.close()
        result=str(open("conditions.txt","r").read())
    return render_template('index.html',result=result)
@app.route('/user.html', methods=['POST'])
def user():
    result = ""
    if request.method == "POST":
        pas=request.form['userpass']
        print(pas)
        con=str(open("conditions.txt", "r").read())
        con=con.split(" ")
        print(con)
        l1=int(con[0])
        l2=int(con[1])
        if(len(pas)<l1 or len(pas)>l2):
            result="Length does not meet requirements"
        pat=['#','@','+','-','%']
        for i in pat:
            if i in pas:
                result=result+"password ok"
        if(result==""):
            result=result+" pattern not matching"
        notallowed=['!','$','*']
        for i in range(2,len(con)):
            notallowed.append(con[i])
        for i in notallowed:
            if i in pas:
                result="contains not allowed patterns"
    return render_template('index.html',result1=result)

if __name__ == '__main__':
    app.run(debug=True)