from flask import *
from subprocess import getoutput
app = Flask(__name__)
@app.route('/')
def root():
    return render_template('home_root.html',flmsgs=get_flashed_messages)
@app.route('/cmd1/<message>',methods=["POST"])
def metthods(message):
    rspp = request.form.get('rsp_path')
    target = request.form.get('path4')
    cmdresult = getoutput(rspp)
    flash(message)
    return redirect(target)
if __name__ == "__main__":
    app.secret_key = "aya567-98979389297329379"
    app.run(debug=True,port=12000)