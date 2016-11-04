from flask import *
from config import app
import checkai_scraper as scraper
jobs = Blueprint('jobs', __name__, template_folder = 'views')
#Exclusions, Skills, Position-type (PM, software dev), Field (AI, Medicine, sports), Experience Level


@jobs.route('/jobs', methods = ['GET'])
def jobs_route_get():
    cur = app.mysql.connection.cursor()
    cur.execute("SHOW TABLES;")
    rv = cur.fetchall()
    print(str(rv))

    sites = 'site:jobs.*.com/* OR site:careers.*.com/* OR site:*.com/careers/* OR site:*.com/jobs/* OR site:*.org/careers/* OR site:*.org/jobs/* OR site:jobs.lever.co/* OR site:boards.greenhouse.io/* OR site:linkedin.com/jobs/view/* -site:dice.com/* -site:indeed.com/* -site:monster.com/* -site:glassdoor.com/* '

    position_type = 'Software Engineer'

    experience_level = 'New Grad'

    fields = ["healthcare", "tech"]

    all_fields = fields[0]
    for field in range(1, len(fields)):
        all_fields+= ' OR ' + fields[field]

    skills = ["iOS", "Swift", "Objective-C"]

    all_skills = '"' + skills[0] + '"'
    for skill in range(1, len(skills)):
        all_skills += ' OR ' + '"' + skills[skill] + '"'

    exclusions = 'Chicago'

    query = sites + position_type + ' "' + experience_level + '"' + ' ' + all_fields + ' ' + all_skills + ' -' + exclusions
    print("QUERY: ", query)


    jobs, summaries, num = scraper.scrape(query)
    return render_template("jobs.html", jobs=jobs, summaries=summaries, num=num)

