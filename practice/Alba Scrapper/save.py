import csv 

def save_to_file(jobs):
    file = open("jobs.csv", mode="w",encoding='utf-8-sig',)
    writer = csv.writer(file)
    writer.writerow(["place","title","time","pay","date"])
    for job in jobs:
        writer.writerow(job.values())
    return

