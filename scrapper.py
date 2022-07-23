from remotely import extract_remotely_jobs
from so import extract_so_url
from indeed import extract_indeed_url


def extract_jobs(word):
  remotely_result = extract_remotely_jobs(word)
  so_result = extract_so_url(word)
  indeed_result = extract_indeed_url(word)
  job_result = remotely_result+so_result+indeed_result
  return(job_result)