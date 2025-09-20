from flask import Flask, render_template, url_for
app = Flask(__name__)

projects_list = [
    {
        'project_title': 'Ductwork installation',
        'project_url': '/img/VBAcode.png',
        'project_desc_para': 'The project required the layout of ductworks in the process plant based on P&ID diagrams. The design team included mechanical, electrical, chemical and structural engineers working in parallel on the design.'
    },
    {
        'project_title': 'Extinguishing kit',
        'project_url': 'assets/img/Ocean Wind/1036507-R-XD-0001_v2.png',
        'project_desc_para': 'The project consisted of the design of a fire extinguishing kit customised according to fire requirements in marine systems.'
    }
]

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def index():
    return render_template('base.html')

@app.route("/projects")
def projects():
    return render_template('projects.html', projects_list=projects_list)

@app.route("/skills")
def skills():
    return "render_template('skills.html')"

@app.route("/education")
def education():
    return "render_template('education.html')"

if __name__ == "__main__":
    app.run(debug=True)