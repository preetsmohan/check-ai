from flask import *
from config import app
pref = Blueprint('pref', __name__, template_folder = 'views')
#Exclusions, Skills, Position-type (PM, software dev), Field (AI, Medicine, sports), Experience Level
from mysql import *

@pref.route('/preferences', methods = ['GET'])
def pref_route_get():
    results = pref_sql("SELECT skills, exclusions, postype, field, explevel FROM user WHERE uid = '{0}'", (session['uid'],))
    
    #init values
    skills = []
    exclusions = []
    postype = []
    field = []
    print(results[0][:4])
    if len(results) and not None in results[0][:4]: #if we have something in the database
        skills = results[0][0].split(";")
        exclusions = results[0][1].split(";")
        postype = results[0][2].split(";")
        field = results[0][3].split(";")
    
    #Next: Pass the values in a Jinja template to populate the HTML rows.
    # print(skills)
    # print(exclusions)
    # print(postype)
    # print(field)
    return render_template("preferences.html", skill_list = skills, exclusion_list = exclusions, postype_list = postype, field_list = field)

@pref.route('/preferences', methods = ['POST'])
def pref_route_post():
    #print request.form
    skills = request.form.getlist('skillz')
    exclusions = request.form.getlist('exclusions')
    postype = request.form.getlist('postype')
    fields = request.form.getlist('fields') 
    
    skills_serialized = ";".join(map(str, skills))
    exclusions_serialized = ";".join(map(str, exclusions))
    postype_serialized = ";".join(map(str, postype))
    fields_serialized = ";".join(map(str, fields))
    pref_sql("UPDATE user SET skills = '{0}', exclusions = '{1}', postype = '{2}', field = '{3}' WHERE uid = '{4}'", (skills_serialized, exclusions_serialized, postype_serialized, fields_serialized, session['uid']))


    #Probably return a redirect instead of a render, redirect to GET this version of the page.
    return redirect("/preferences")
