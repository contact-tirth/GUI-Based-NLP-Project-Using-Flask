from http.client import responses

from flask import Flask, render_template, request
from db import Database as dbo, Database
import nlpcloud

app = Flask(__name__)
dbo = Database()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('signup.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    response = dbo.insert(name,email,password)

    if response:
        return render_template('login.html',message='Registration Sucessfull!')
    else:
        return render_template('signup.html',message='User is already registered!')

@app.route('/login_page',methods=['post'])
def login_page():
    email_1 = request.form.get('email_1')
    password_1 = request.form.get('password_1')

    response_1 = dbo.search(email_1,password_1)
    if response_1:
        return render_template('login_page.html')
    else:
        return render_template('login.html',message='Invalid Id/Password')

@app.route('/api_call')
def api_call():
    return render_template('code_generation.html')

@app.route('/perform_cg',methods=['post'])
def perform_cg():
    text_val=request.form.get('text')
    print(text_val)
    result = generate_code_api_response(text_val)
    print(result)
    final_result=result['generated_code']

    return render_template('code_generation.html',result=final_result)

def generate_code_api_response(text_val):
    # string_instruction_val = self.text_box.get("1.0", tkinter.END)
    text_v=text_val
    client = nlpcloud.Client("finetuned-llama-3-70b", "25c8717fab9a0a2dddf4c31e1b09531480e548ec", gpu=True)
    code=client.code_generation(
           text_v
    )
    return code

if __name__=='__main__':
    app.run(debug=True)