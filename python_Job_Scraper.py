import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://google.com"
}

url = "https://realpython.github.io/fake-jobs/"


res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

# Find all job cards
jobs = soup.find_all("div", class_="card-content")
print(f"Total jobs found: {len(jobs)}")

# Extracting data 
data = []

for job in jobs:
    title_elem = job.find("h2", class_="title")
    company_elem = job.find("h3", class_="company")
    location_elem = job.find("p", class_="location")
    
    parent = job.parent
    link = parent.find("a")["href"] if parent and parent.find("a") else "N/A"
    
    title = title_elem.text.strip() if title_elem else "N/A"
    company = company_elem.text.strip() if company_elem else "N/A"
    location = location_elem.text.strip() if location_elem else "N/A"
    
    data.append([title, company, location, link])
    
    #first job as an example to print
    if len(data) == 1:
        print("\n--- First Job Example ---")
        print(f"Title: {title}")
        print(f"Company: {company}")
        print(f"Location: {location}")
        print(f"Link: {link}\n")

# Saving 
with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Company", "Location", "Link"])
    writer.writerows(data)

# Final output
print(f"✅ Successfully saved {len(data)} jobs to jobs.csv")


