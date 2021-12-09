import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["job_search"]

mycol = mydb["job_posting_sites"]

#add column for url to job search page itself
mylist = [
    { "name": "Indeed", "url", "https://www.indeed.com/"}
    { "name": "LinkedIn Jobs", "url", "https://www.linkedin.com/jobs/"}
    { "name": "Monster", "url": "https://www.monster.com/"}
    { "name": "CareerBuilder", "url": "https://www.careerbuilder.com/"}
    { "name": "Brooksource", "url": "https://jobs.brooksource.com/"}
    { "name": "TEKsystems", "url": "https://careers.teksystems.com/us/en"}
]

exec = mycol.insert_many(mylist)
