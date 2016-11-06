from flask import *
from config import app
import scrapers as scraper
from mysql import *
jobs = Blueprint('jobs', __name__, template_folder = 'views')
#Exclusions, Skills, Position-type (PM, software dev), Field (AI, Medicine, sports), Experience Level


@jobs.route('/jobs', methods = ['GET'])
def jobs_route_get():

    sites = '-site:yelp.com/* -site:dice.com/* -site:indeed.com/* -site:monster.com/* -site:glassdoor.com/ -site:jobs.climber.com/* site:jobs.*.com/* OR site:careers.*.com/* OR site:*.com/careers/* OR site:*.com/jobs/* OR site:*.org/careers/* OR site:*.org/jobs/* OR site:jobs.lever.co/* OR site:boards.greenhouse.io/* OR site:linkedin.com/jobs/view/* '

    results = pref_sql("SELECT skills, exclusions, postype, field, explevel FROM user WHERE uid = '{0}'", (session['uid'],))

    if len(results) and not None in results[0][:4]: #if we have something in the database
        skills = results[0][0].split(";")
        print(skills)
        exclusions = results[0][1].split(";")
        print(exclusions)
        postype = results[0][2].split(";")
        print(postype)
        fields = results[0][3].split(";")
        print(fields)
    
    experience_level = ''

    all_fields = fields[0]
    for field in range(1, len(fields)):
        if fields[field] != '':
            all_fields+= ' OR ' + fields[field]
    all_positions = postype[0]
    for pos in range(1, len(postype)):
        if postype[pos] != '':
            all_positions += ' ' + postype[pos]
    all_exclusions = exclusions[0]
    for exclusion in range(1, len(exclusions)):
        if exclusions[exclusion] != '':
            all_exclusions+= ' -' + exclusions[exclusion]
    
    all_skills = '"' + skills[0] + '"'
    for skill in range(1, len(skills)):
        if skills[skill] != '':
            all_skills += ' OR ' + '"' + skills[skill] + '"'

    query = sites + all_positions + ' "' + experience_level + '"' + ' ' + all_fields + ' ' + all_skills + ' -' + all_exclusions
    print("QUERY: ", query)


    jobs, summaries, num = scraper.scrape(query)
    return render_template("jobs.html", jobs=jobs, summaries=summaries, num=num, signedIn=True)

