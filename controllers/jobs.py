from flask import *
from config import app
import scrapers as scraper
from mysql import *
jobs = Blueprint('jobs', __name__, template_folder = 'views')
#Exclusions, Skills, Position-type (PM, software dev), Field (AI, Medicine, sports), Experience Level


@jobs.route('/jobs', methods = ['GET'])
def jobs_route_get():

    sites = 'site:jobs.*.com/* OR site:careers.*.com/* OR site:*.com/careers/* OR site:*.com/jobs/* OR site:*.org/careers/* OR site:*.org/jobs/* OR site:jobs.lever.co/* OR site:boards.greenhouse.io/* OR site:linkedin.com/jobs/view/* -site:dice.com/* -site:indeed.com/* -site:monster.com/* -site:glassdoor.com/* '

    results = pref_sql("SELECT skills, exclusions, postype, field, explevel FROM user WHERE uid = '{0}'", (session['uid'],))

    if len(results) and not None in results[0][:4]: #if we have something in the database
        skills = results[0][0].split(";")
        exclusions = results[0][1].split(";")
        postype = results[0][2].split(";")
        fields = results[0][3].split(";")
    
    experience_level = 'New Grad'

    all_fields = fields[0]
    for field in range(1, len(fields)):
        all_fields+= ' OR ' + fields[field]

    all_exclusions = exclusions[0]
    for exclusion in range(1, len(exclusions)):
        all_exclusions+= ' -' + exclusions[exclusion]
    
    all_skills = '"' + skills[0] + '"'
    for skill in range(1, len(skills)):
        all_skills += ' OR ' + '"' + skills[skill] + '"'

    query = sites + str(postype[0]) + ' "' + experience_level + '"' + ' ' + all_fields + ' ' + all_skills + ' -' + all_exclusions
    print("QUERY: ", query)


    jobs, summaries, num = scraper.scrape(query)
    return render_template("jobs.html", jobs=jobs, summaries=summaries, num=num)

