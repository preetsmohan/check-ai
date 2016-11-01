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
    jobs, summaries, num = scraper.scrape('site:jobs.lever.co/* OR site:boards.greenhouse.io/* OR site:linkedin.com/jobs/view/* OR site:ziprecruiter.com/* software OR engineer OR developer "healthcare technology" OR "medical devices" "technology" "objective-c" OR "swift" OR "iOS" -android ')
    return render_template("jobs.html", jobs=jobs, summaries=summaries, num=num)

