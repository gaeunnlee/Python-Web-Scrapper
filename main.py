from flask import Flask, render_template, request, redirect

from scrapper import extract_jobs

app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        jobs = extract_jobs(word)
        existingJobs = db.get(word)
        if existingJobs:
          jobs = existingJobs
        else:
          jobs = extract_jobs(word)
          db[word] = jobs
    else:
        return redirect("/")

    return render_template("report.html",
                                   
  searchingBy=word,
  resultNumber=len(jobs),
  jobs = jobs
)


app.run(host="0.0.0.0")
