from flask import Flask, render_template, jsonify


app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Kenya',
        'salary': 'ksh 120000' 
    },
    {
        'id': 2,
        'title': 'Backend Developer',
        'location': 'USA',
        'salary': '$1200k' 
    },
    {
        'id': 3,
        'title': 'Frontend Developer',
        'location': 'Remote',
        'salary': 'ksh 120000' 
    }
]

@app.route("/")
def show():
    return render_template("home.html", jobs=JOBS, company_name = "Ndegwa")

@app.route("/api/jobs")
def job_list():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)