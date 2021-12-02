from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def default():
    return render_template('index2.html', columns=8, rows=8)
@app.route('/<int:columns>')
def columns(columns):
    return render_template('index2.html', columns=int(columns), rows=8)
@app.route('/<int:columns>/<int:rows>')
def column(columns, rows):
    return render_template('index2.html', columns=int(columns), rows=int(rows))
@app.route('/<int:columns>/<int:rows>/<colorOne>/<colorTwo>')
def colors(columns, rows, colorOne, colorTwo):
    return render_template('index2.html', columns=int(columns), rows=(int(rows)), colorOne=str(colorOne), colorTwo=str(colorTwo))
if __name__ == "__main__":
    app.run(debug=True)