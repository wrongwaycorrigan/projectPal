"""work.py: this is where all the magic happns"""

import os
import shutil
import configparser
import logging
import glob
import re

#set up config to read variables in ini file
config = configparser.ConfigParser()
config.read('projp.ini')

def create_project_dirs(pth):
    """Create directory structure for project or shot. It takes an argument to the path of the new dir structure
        and an argument to the type of project"""

    #Read the ini file for the universalsubs, create a dir for each entry
    if 'universalsubs' in config:
        #not sure about this try except. Should it return?
        try:
            #make project root dir
            logging.info("creating master project dir " + pth)
            os.mkdir(pth)
            #make sub dirs
            for value in config['universalsubs'].values():
                new_dir = os.path.join(pth, value)
                logging.info("creating subdir " + new_dir)
                os.mkdir(new_dir)
            return True
        except OSError as ose:
            logging.error(ose)
            return False #does this make sense?
    else:
        #This error writes to a log so the admin can read it. The end user might not be interested.
        logging.error("Could not read universalsubs section of ini file.")
        return False

def add_project_templates(project_path, project_type):
    """Adds project templates files to the new project folders. The project_path arg is the path to the project, the project_type arg
        is the type of project"""
    logging.debug("project path " + project_path + " project type " + project_type)
    template_root = config['templateroot']['root']
    template_src_dirs = config['templatesrcdirs']
    template_dest_dirs = config['templatedestdirs']
    #loop over template source types
    for program, directory in template_src_dirs.items():
        #maybe this captures too much. Need to narrow it down a bit.
        try:
            src_dir = os.path.join(template_root, directory)
            # glob expression to grab all relavent files starting with type name
            expression = project_type + '*'
            logging.debug("var expression " + expression)
            src_files = glob.glob(os.path.join(src_dir, expression))
            logging.debug("var src_files " + str(src_files))
            logging.debug("var template_dest_dir " + template_dest_dirs[directory])
            logging.info("Looking to move files " + str(src_files))
            for file_path in src_files:
                file_name = os.path.basename(file_path)
                logging.debug("var file_name" + file_name)
                src_file_name = os.path.join(src_dir, file_name)
                logging.debug("src_file_name " + src_file_name)
                project_name = os.path.basename(project_path)
                #The new file name is named after the project
                new_file_name = re.sub(project_type, project_name, file_name)
                dest_file_name = os.path.join(project_path, template_dest_dirs[directory], new_file_name)
                logging.debug("dest_file_name " + dest_file_name)
                logging.info("Adding file " + src_file_name + " to project as " + dest_file_name)
                if (os.path.isfile(src_file_name)):
                    shutil.copy(src_file_name, dest_file_name)
        #Need to define template exception
        except Exception as te:
            logging.error(te)
            return False
    return True

def create_project(pth, tp):
    """Wrapper function used to check success of create_project_dirs and add_project_templates"""
    logging.info("Attempting to create new project...")
    if create_project_dirs(pth) and add_project_templates(pth, tp):
        logging.info("Successfully added project " + pth)
        return True
    else:
        #remove directory tree that was created and return False
        logging.error("Something went wrong in the creation of the project. Cleaning up...")
        if os.path.exists(pth):
            shutil.rmtree(pth)
        return False

