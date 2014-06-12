import os
import shutil
import configparser
import logging
import glob
import re

def create_shot_dirs(pth, tp):
    """Create directory structure for a new shot. It takes an argument to the path of the project
        and an argument of the type"""
    print("in create_shot_dirs()")
    return True

def add_shot_templates(pth, tp):
    """Adds shot templates to a project. The pth arg is the path to the shot, the tp arg
        is the type of project"""
    print("in add_shot_templates()")
    return True

#NEED TO MODIFY THE FOLLOWING FUNCTION TO ACCOMODATE SHOTS INSTEAD OF PROJECTS=================================================
def create_shot(pth, tp):
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

