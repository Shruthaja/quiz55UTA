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

if __name__ == '__main__':
    app.run(debug=True)