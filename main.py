from flask import Flask, render_template, request, redirect, send_file
from scrapper import extract_jobs
from exporter import save_to_files

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

@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    if not word: # if word doesn't exist
      raise Exception() # it will be exception
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_files(jobs)
    return send_file("jobs.csv")
  except:
    return redirect("/") # redirect to home

    

app.run(host="0.0.0.0")
