import flask

app = flask.Flask("NeoPear")

@app.route('/')
def main_page():
    return '<div style="position:fixed;top:50%;left:50%;transform:translate(-50%,-50%)">NeoPear</div>'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
