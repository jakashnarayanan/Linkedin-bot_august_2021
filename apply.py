
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json
import xlwt as xw
from datetime import datetime
import random
import time
import math

class Eassyapplylinkedin:
    ##intilaizes the class with the json file
    def __init__(self,data):
        self.email = data['email']
        self.password = data['password']
        self.keywords = data['keywords']
        self.location = data['location']
        self.level = data['level']
        self.jobs_per_page = 25
        self.driver=webdriver.Chrome(data['path'])
        excel = xw.Workbook()
        applied =excel.add_sheet('jobs applied')
        self.not_applied = excel.add_sheet('jobs could not be applied')
        
        #excel.save('job.xls')

 
    #   fucntion gets you login inside the linkedin  
    def login_linkedin(self):
        self.driver.get("https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in")

        username = self.driver.find_element_by_name("session_key")
        username.clear()
        username.send_keys(self.email)
        password = self.driver.find_element_by_name("session_password")
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
    ##This function has beem assigned for future works
    def entry(self):

        if self.level == "internship":
            row = "1"  
        elif self.level == "Entry_level":
            row = "2"
        elif self.level == "assosicate":
            row ="3"         
        return row
    ##Works as per the filters applied dont forget to give the name as excact as in linkedin. 
    def filter(self):
        
        time.sleep(1)
        ##filter section
        self.driver.get("https://www.linkedin.com/jobs/search/?distance=25&f_AL=true&geoId=115702354&keywords="+self.keywords+"&location="+self.location)
    ##Goes through filter result gets all the jobs available and creates a list
    def get_jobs(self):
        total_results = self.driver.find_element_by_class_name("display-flex.t-12.t-black--light.t-normal")
        total_results_int = int(total_results.text.split(' ',1)[0].replace(",",""))
        # get results for the first page
        current_page = self.driver.current_url
        results = self.driver.find_elements_by_class_name("jobs-search-results__list-item.occludable-update.p0.relative.ember-view")
        print("waiting")
        print(len(results))
        time.sleep(3)
        
        
        for result in results:

            print(result)
            hover = ActionChains(self.driver).move_to_element(result)
            hover.perform()
            titles = result.find_elements_by_class_name('full-width.artdeco-entity-lockup__title.ember-view')
            print(titles)
            
            for title in titles:
                print("getting into second for loop")
                self.submit_apply(title)
                #excel.save('job.xls')    
                print("all possible jobs has been applied")
                
    ## all the various possibiity that will be faced by the bot has been mentioned, may miss something that can cause error 
    ##feel free to comment the bugs your facing so i can tune this section for better
    def submit_apply(self,job_add):
    

        print('You are applying to the position of: ', job_add.text)
        job_add.click()
        time.sleep(2)
        
        # click on the easy apply button, skip if already applied to the position
        try:
            print("checking for easy apply button")
            time.sleep(2)
            in_apply = self.driver.find_element_by_xpath("//button[@data-control-name='jobdetails_topcard_inapply']")
            in_apply.click()
            try:
                time.sleep(1)
                submit = self.driver.find_element_by_xpath("//button[@data-control-name='submit_unify']")
                submit.click()
                time.sleep(1)
                try:
                    wait = WebDriverWait(self.driver, 10)
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label=Dismiss]"))).click()
                    #self.applied.write(a+1,0,job_add.text + '-' + self.driver.current_url + str(datetime.now()))
                except:
                    #self.applied.write(a+1,0,job_add.text + '-' + self.driver.current_url + str(datetime.now()))
                    pass   

        # ... if not available, discard application and go to next
            except NoSuchElementException:
                print('Not direct application, going to next...')
                try:
                    conti = self.driver.find_element_by_xpath("//button[@data-control-name='continue_unify']")
                    conti.send_keys(Keys.RETURN)
                    time.sleep(2)
                    try:
                        summit = self.driver.find_element_by_xpath("//button[@data-control-name='submit_unify']")
                        summit.send_keys(Keys.RETURN)
                        try:
                            wait = WebDriverWait(self.driver, 10)
                            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label=Dismiss]"))).click()
                            #self.applied.write(a+1,0,job_add.text + '-' + self.driver.current_url + str(datetime.now()))
                        except:
                            #self.applied.write(a+1,0,job_add.text + '-' + self.driver.current_url + str(datetime.now()))
                            pass

                        return
                    except:

                        conti.send_keys(Keys.RETURN)
                       

                        time.sleep(2)

                        
                        try:
                            for ele in self.driver.find_elements(By.CSS_SELECTOR, "div.fb-single-line-text input"):
                                time.sleep(1)
                                ele.clear()
                                ele.send_keys(random.randint(0,1))

                            try:
                                conti.send_keys(Keys.RETURN)
                                try:
                                    summit = self.driver.find_element_by_xpath("//button[@data-control-name='submit_unify']")
                                    summit.send_keys(Keys.RETURN)
                                    
                                except:
                                    pass

                                

                            except:
                                pass
                        except:
                            summit = self.driver.find_element_by_xpath("//button[@data-control-name='submit_unify']")
                            summit.send_keys(Keys.RETURN)
                            try:
                                wait = WebDriverWait(self.driver, 10)
                                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label=Dismiss]"))).click()
                                #self.applied.write(a+1,0,job_add.text + '-' + self.driver.current_url + str(datetime.now()))
                                return
                            except:
                                #self.applied.write(a+1,0,job_add.text + '-' + self.driver.current_url + str(datetime.now()))
                                return
                                pass

                       

                        

                    try:
                        review = self.driver.find_element_by_xpath("//button[@data-control-name='review_unify']")
                        review.send_keys(Keys.RETURN)
                        time.sleep(2)
                        summit = self.driver.find_element_by_xpath("//button[@data-control-name='submit_unify']")
                        summit.send_keys(Keys.RETURN)
                        time.sleep(1)
                        try:

                            wait = WebDriverWait(self.driver, 10)
                            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label=Dismiss]"))).click()
                            #self.applied.write(a+1,0,job_add.text + '-' + self.driver.current_url + str(datetime.now()))
                        except:
                            #self.applied.write(a+1,0,job_add.text + '-' + self.driver.current_url + str(datetime.now()))
                            pass
                
                    except :
                        close_button = self.driver.find_element_by_xpath("//button[@data-test-modal-close-btn='']")
                        close_button.send_keys(Keys.RETURN)
                        time.sleep(1)
                        discard = self.driver.find_element_by_xpath("//button[@data-control-name = 'discard_application_confirm_btn']")
                        discard.send_keys(Keys.RETURN)
                        #self.not_applied.write(b+1,1,job_add.text + '-'+ self.driver.current_url + str(datetime.now()))
                        #excel.save('job.xls') 
                        
                except:
                    close_button = self.driver.find_element_by_xpath("//button[@data-test-modal-close-btn='']")
                    close_button.send_keys(Keys.RETURN)
                    time.sleep(1)
                    discard = self.driver.find_element_by_xpath("//button[@data-control-name = 'discard_application_confirm_btn']")
                    discard.send_keys(Keys.RETURN)
                    #self.not_applied.write(b+1,1,job_add.text + '-'+ self.driver.current_url + str(datetime.now()))
                    #excel.save('job.xls') 

        except NoSuchElementException:
            print('You already applied to this job, go to next...')
            #self.not_applied.write(1+b,1,job_add.text + '-'+ self.driver.current_url + str(datetime.now()))
            #excel.save('job.xls')
            
        

        # try to submit if submit application is available...
        
            
        time.sleep(1)
if __name__ == "__main__":
    a=0
    b=0
    #excel = xw.Workbook()
    #applied =excel.add_sheet('jobs applied')
    #not_applied = excel.add_sheet('jobs could not be applied')

    with open('config.json') as config_file:
        data = json.load(config_file)
    
    bot = Eassyapplylinkedin(data)
    bot.login_linkedin()
    time.sleep(2)
    bot.filter()
    time.sleep(1)
    bot.get_jobs()