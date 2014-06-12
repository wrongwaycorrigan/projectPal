from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(6)

    def tearDown(self):
        self.browser.quit()

    def test_create_project_on_local_machine(self):
        #Penguin has heard about a site for creating project directories and files.
        #He goes to the homepage.
        self.browser.get('localhost:8000')
        self.assertIn('Project Pal', self.browser.title)

        #He enters the name of a project in the text field, chooses a project type and presses the button.
        #Everything goes ok and he is redirected to the successful page that lists his project.

        #The project directories are created on the local machine.


    def test_create_project_fails_with_duplicate_name(self):
        #Penguin goes to the project pal homepage 
        self.browser.get('localhost:8000')

        #He enters the name of a project in the text field that already exists.
        #An error occurs and he is redirected to the page that tells him about the mistake



if __name__ == "__main__":
    unittest.main(warnings='ignore')
