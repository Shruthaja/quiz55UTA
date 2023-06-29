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
        con=open("conditions.txt",'r').read()
        con=con.split()
        result=""
        forbid=['!','@','$','*']
        for i in range(2,len(con)):
            forbid.append(con[i])
        if(len(pas)>=int(con[0]) and len(pas)<=int(con[1])):
            regex = ('(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%^&+=])(?=\S+$).{8,}$')
            p = re.compile(regex)
            result=p.match(pas)
            for i in forbid:
                if i in pas:
                    result=""
            if(result==""):
                result="does not meet pattern requirement"
        else:
                result="does not meet length"
    return render_template('index.html',result1=result)

if __name__ == '__main__':
    app.run(debug=True)