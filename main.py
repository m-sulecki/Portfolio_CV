from flask import Flask, render_template, url_for
app = Flask(__name__)

projects_list = [
    {
        'project_title': 'Ductwork installation',
        'project_url': 'img/SCR/SCR unit.png',
        'project_desc_para': 'The project required the layout of ductworks in the process plant based on P&ID diagrams. The design team included mechanical, electrical, chemical and structural engineers working in parallel on the design.'
    },
    {
        'project_title': 'Extinguishing kit',
        'project_url': '/img/Ocean Wind/1036507-R-XD-0001_v2.png',
        'project_desc_para': 'The project consisted of the design of a fire extinguishing kit customised according to fire requirements in marine systems.'
    },
    {
        'project_title': 'Piping process installation',
        'project_url': '/img/DilutionSkids/Scenario 9.18.07.png',
        'project_desc_para': 'The project required the design of a complete process installation layout based on P&ID diagrams. The scope of the project included the design of pipe routing, specifying the position of the required instrumentation based on ATEX and pharmaceutical industry standards.'
    },
    {
        'project_title': 'Washing pallet',
        'project_url': '/img/paletka_DS/438.0953_00.png',
        'project_desc_para': 'The tooling was used to position components in the inter-operational spray washing process.'
    },
    {
        'project_title': 'Antenna redesign',
        'project_url': '/img/Carbon to Aluminium/antena.PNG',
        'project_desc_para': 'Antena lorem ipsum redesign'
    },
    {
        'project_title': 'Buffer tank configurator',
        'project_url': '/img/iLogic/Buffer Tank No. 1 - 200 m3_ilogic.png',
        'project_desc_para': 'The project was to create an assembly configurator, which enabled the customer to generate new versions of the tank with different dimensions, number of process connections and their location in an user-friendly way.'
    },
    {
        'project_title': 'Shrink connection',
        'project_url': '/img/Abaqus_interference_torque/torque.png',
        'project_desc_para': 'lorme ispum'
    },
    {
        'project_title': 'Headphones',
        'project_url': '/img/Headphones/17861-110001.png',
        'project_desc_para': 'lorem ispum'
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