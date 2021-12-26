# Linkedin-bot_august_2021
This repo helps you apply for all jobs of your intrest on linkedin by just a click.

The modification till august 2021 has been made for find_by_element (in selenium).where lot has been changed in linkedin HTML code recently


Step 1:
So how to use this repo:
First you need a 
[1)python3
2)selenium library
3)json
4)xlwt
5)radnom
6)time
7)math](url)
yes there is been lot lot going here. As linkedin has taken lots of steps to prevent bots), so you need all the libraries mentioned above

Step2:

And you need web browser of your choice. And just add the browser path to the line 7 on  config.json file under the section path
also mention ur browser name on the line 28 on the python file apply.py. 
[self.driver=webdriver.Chrome(data['path'])](url)

just replace the word chrome with browser driver that you have downloaded. if ur using chrome fine just leave that as of.

Also add path of your config.json file to the line 230 of apply.py

Step 3:
We are almost done

Enter your details on the config.json file. your email id  , password all the mentioned details. And more importantly dont forget to type correct spelling for the label level.

To brief:
[{
    "email" : "elisharoni040@gmail.com",
    "password" : "samsung5565",
    "keywords" : "html",
    "location" : "chennai",
    "level" : "internship", 
    "path" : "D:\\chromedriver.exe"
}](url)

on label level where the intenrship has been mentioned.Linkedin allows you to choose between 6 level of experiance naming such as internship,entry level , assocaiate and so on. while entering your experiance level try to spell it correct.(i have already using tons of library i dont want to use another to check teh spells)

Step 4:
under your linkedin make sure ur resume has been uploaded. the bot uses only the resume that has been uploaded on the linkeddin

Step 5:
Thats all you can now apply by just one click.



Pros:
1)i have developed as it dont crash , as you know linkedin trying its best for avoiding bots into its system . So the bot i have developed can tackle 95 % of it as for the various test run i had made.

2)and some of the left out question such as your experiance level on this languages . will be randomly answered ranging 0,1 . (some people may dont want it feel free to comment it out)

Cons:
 The part i can write thousand words
 1)the sytem does not crash. but its applying rate is low must be some where 40%.
 2)The reason the system cannot answer the questions for drop down box and multiple choise question. which has been often asked by the companies(it can be solved, hope i sort this out )
 3)And there can be bugs i missed feel free to comment it out.
 
 future works:
 1)there has been a feature commented out on the code . which can enter the job that has been applied and not applied into a excel sheet. with the link . it would be easy to identify the jobs that has applied and the jobs that has not applied can be applied manually.
 
 last words:
 its for education purpose only dont try to misuse it. Linkedin has mentioned in their terms and condition if thery find you using bots they may ban ur id.(i have been testing my bot for 100 times now. they could not find it though). But dont try to misuse it and always rember you may get banned.
