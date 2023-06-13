from flask import Flask, render_template


app = Flask(__name__)


@app.route('/index.html')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/about.html')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/classes.html')
def classes():  # put application's code here
    return render_template('classes.html')

@app.route('/feature.html')
def feature():  # put application's code here
    return render_template('feature.html')

@app.route('/quote.html')
def quote():  # put application's code here
    return render_template('quote.html')

@app.route('/contact.html')
def contact():  # put application's code here
    return render_template('contact.html')

@app.route('/project.html')
def project():  # put application's code here
    return render_template('project.html')

@app.route('/service.html')
def service():  # put application's code here
    return render_template('service.html')

@app.route('/team.html')
def team():  # put application's code here
    return render_template('team.html')

@app.route('/testimonial.html')
def testimonial():  # put application's code here
    return render_template('testimonial.html')






if __name__ == '__main__':
    app.run()

