from app import create_app, extensions
from flask import render_template
app = create_app()

@app.route('/')
def index():
    actions = list(extensions.get())
    actions.reverse()
    return render_template('index.html', actions =actions[:15])

if __name__ == '__main__': 
    app.run(port = 80,debug=True)
