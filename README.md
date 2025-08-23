# End-to-End-Data-Analysis-Project-of-Job-Market-in-Ireland
This repository contains data analysis and cleaning scripts for job market research in Ireland. The focus is on Data Analyst, Data Engineer, and Data Scientist roles. All code is written in Python and is easy to understand.
And you can find my dashboard in Tableau public at https://public.tableau.com/app/profile/tianyi.ren4423/viz/Dashboard_17557400021050/Dashboard?publish=yes

# 1.Project Requirements
This project is a demo that mean to understand the job market of data ralated jobs (data analyst, data engineer, data scientist) in Irenland of July 2025, and all my data come fron IrishJob.ie. Detail of the project can be found in the Project_Requirements_Document.pdf.

# 2.Data collection plan
Coming to the next step, I make a plan of data collection, collect data include job type,average salary, job locations, skills neede ect.. All that can be found in Data_Collection_Plan.pdf.

# 3.Design of the Dashboard
After the early preperation jobs, I designed a draft of the dashboard and can be found in this project menu too.

# 4.Data collections and cleaning
I use web scrapting to collect the raw data I need (code is in folder Code_pythonScrapting). And I cleaned it and reorganized it in the format that can be used in Tableau (code in folder Code_pythonDataCleaning). Raw data and clean data is storaged at the 'dataset' folder. I collected the address of each job and converted it to longitude and latitude coordinates. I also collected the company names and used dictionary substitution to replace them with various categories for statistical purposes. For salary and average salary, I used data from the National Bureau of Statistics. For skills and work experience, I went into each job description, extracted skill keywords, and counted their frequency. For experience, I used the keyword (experience) to index the text before and after, generally indexing English and Arabic numerals as the final result.

# 5.Data visualization
I use Tableau public to go with visualization and get the dashboard done.

# 6.Data Analysis report
You can read my report in the Report.pdf.
