from flask import Flask, render_template, request, redirect

app = Flask(__name__)
    
@app.route('/')
def my_home():
    # we can render html file like this.
    # it looks for it in the templates folder
    return render_template('index.html')

@app.route('/<string:page_name>')
def route_page(page_name='index'):
    return render_template(page_name)

def write_to_file(data):
    with open('contactdata.txt', mode='a') as contact_data_file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = contact_data_file.write(f'\n{email},{subject},{message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('thankyou.html')
    else:
        return 'something went wrong. Try again !'

# @app.route('/index.html')
# def index():
#     return render_template('index.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')
    
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
    
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/<username>/<int:post_id>')
# def hello_user(username=None, post_id=None):
#     return render_template('index.html', username = username, post_id = post_id)

# @app.route('/blog')
# def blog():
#     return 'Blog here!'

# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'This is my dog!'
