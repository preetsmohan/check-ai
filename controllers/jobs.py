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

    sites = 'site:jobs.lever.co/* OR site:boards.greenhouse.io/* OR site:linkedin.com/jobs/view/* OR site:ziprecruiter.com/* '

    position_type = 'project manager'

    experience_level = "senior"

    field = "finance"

    skills = ["C++", "operating systems", "python"]

    all_skills = '"' + skills[0] + '"'
    for skill in range(1, len(skills)):
        all_skills += ' OR ' + '"' + skills[skill] + '"'

    exclusions = 'apple'

    query = sites + position_type + ' "' + experience_level + '"' + ' "' + field + '" ' + all_skills + '-' + exclusions
    print("QUERY: ", query)


    jobs, summaries, num = scraper.scrape(query)
    return render_template("jobs.html", jobs=jobs, summaries=summaries, num=num)

