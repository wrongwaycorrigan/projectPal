"""Project Pal: A web based app that creates a directory structure for a project and populates the appropriate directories with templates for
    that specific type of project.
    This is the front end piece written in bottle.
    """

from bottle import get, post, request, route, run, template, static_file, redirect
from create_project import *
import os

#set up logging
logging.basicConfig(filename='logs/projectPal.log', level=logging.DEBUG, format='%(asctime)s %(funcName)s:line %(lineno)s: %(message)s')

#This is the root directory where all the projects will live:
#It's read from the ini file
#look this up, possible namespace conflict with create_project.py config===========================
config = configparser.ConfigParser()
config.read('projp.ini')
project_root = config['projectroot']['root']
static_folder = '/Users/rob/Documents/work/projectpal/static'
#====================================================================

@route('/static/<filepath:path>')
def server_static(filepath):
    """Serves the static data. Change root location below if necessary."""
    print(static_folder)
    return static_file(filepath, root=static_folder)


@get('/')
def index():
    return template('index', projects = os.listdir(project_root))

@route('/nameexists/<project_name>')
def name_exists(project_name=''):
    return template('nameexists', projects=os.listdir(project_root), project_name=project_name)

@route('/successful/<project_name>')
def successful_add(project_name=''):
    return template('success', project_name=project_name)

@route('/unsuccessful/<project_name>')
def unsuccessful_add(project_name=''):
    return template('nosuccess', projects=os.listdir(project_root), project_name=project_name)

@route('/forbidden')
def forbidden_name(project_name=''):
    return template('forbidden', projects=os.listdir(project_root), project_name=project_name)

@route('/shot/<shot_name>')
def create_new_shot(shot_name=''):
    return template('shot', projects=os.listdir(project_root), shot_name=shot_name)

@post('/submitproject')
def create_new_project():
    global project_root
    project_name = request.forms.get('project_name')
    project_type = request.forms.get('project_type')
    machine_name = request.forms.get('destination')

    #if project already exists, redirect
    if project_name in os.listdir(project_root):
        redirect('nameexists/' + project_name)

    if project_name == ".DS_Store" or project_name == "Thumbs.db":
        redirect('forbidden')

    #if machine is a different machine, add it to the project_root as unc path before creating project
    #This needs to be fixed to add the unc path
    if machine_name != "local":
        project_root = os.path.join(machine_name, project_root)

    #create project
    if create_project(os.path.join(project_root, project_name), project_type):
        redirect('successful/' + project_name)
    else:
        redirect('unsuccessful/' + project_name)

run(host='localhost', port=8000, reloader=True, debug=True)

@post('/submitshot')
def create_new_shot():
    #modify from project to shot===========================================================
    global project_root
    project_name = request.forms.get('project_name')
    shot_name = request.forms.get('shot_name')
    machine_name = request.forms.get('destination')

#is this necessary? if no project, how would we get to this page (other than url)==========================================================
    #if project doesn't already exists, redirect
    if project_name not in os.listdir(project_root):
        redirect('projectnoexist/' + project_name)
#--------------------------------------------------------------------------------

    if project_name == ".DS_Store" or project_name == "Thumbs.db":
        redirect('forbidden')

    #if machine is a different machine, add it to the project_root as unc path before creating project
    #This needs to be fixed to add the unc path
    if machine_name != "local":
        project_root = os.path.join(machine_name, project_root)

    #create project
    if create_shot(os.path.join(project_root, project_name), project_type):
        redirect('successful/' + shot_name)
    else:
        redirect('unsuccessful/' + shot_name)

run(host='localhost', port=8000, reloader=True, debug=True)
