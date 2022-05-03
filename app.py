from flask import Flask


from flask import (
    Blueprint, 
    flash,  
    redirect, 
    render_template, 
    request, url_for
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/indicadores",methods=['POST'])
def indicadores():
    if request.method == 'POST':
        data = request.form.get('data')
        
    return render_template('/indicadores.html', data=data)


app.run(
    debug=True
)