from flask import Flask, request, jsonify, render_template
import turtle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    shape = data['shape']
    generate_shape(shape)
    return jsonify(success=True)

def generate_shape(shape):
    screen = turtle.Screen()
    t = turtle.Turtle()

    if shape == 'circle':
        t.circle(50)
    elif shape == 'square':
        for i in range(4):
            t.forward(100)
            t.right(90)
    elif shape == 'triangle':
        for i in range(3):
            t.forward(100)
            t.right(120)
    elif shape == 'pentagon':
        for i in range(5):
            t.forward(100)
            t.right(72)
    screen.mainloop()

if __name__ == '__main__':
    app.run(debug=True)