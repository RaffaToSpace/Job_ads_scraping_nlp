# Analysis of job ads for _Data Scientist_ roles from job boards
## Intro
A tech recruiter recently posted on LinkedIn asking for tips on learning resources to recommend to perspective data scientists, in order to acquire the right skills for today's market. She received many replies to her post, most of them suggesting the usual set of online learning services, plus some general recommendation, e.g. practice coding interviews,  try a Kaggle competition, etc.  
I thought: how can I gather useful information about what are the most requested skills in the job market right now? As a data science newcomer, I have felt a bit desperate at times as I try to chase the market, picking new projects or learning materials depending on what I see (or I think I see) more commonly on the job ads, or on what I am asked at interviews.  
I have decided to take a step forward, and find out for myself: in this project I am collecting a number of job descriptions from a popular job board website, in order to find out what are the recurring key words in them, which ones correspond to acquirable skills, and how (and if) they correlate to details such as the job salary, contract type and others.
It is an open ended project, as the information acquired depends on the moment and will change over time, and the analysis can be done on many different levels.

I have written about this project on my [post](https://towardsdatascience.com/how-to-identify-the-most-requested-skills-on-the-data-science-job-market-with-data-science-726845ca9638) on Towards Data Science. Please check the post to read about the thinking process behind the project, the outcomes and the project conclusions and possible future developments.

## Project description
In this project I am scraping job ads contents from a popular job board to gather insights on the key skills listed and other factors. The project is structured as follows:

- **Job ads scraping** notebook: scraping of job descriptions and other information (salary, location, type of contract), saved in a JSON format for ease of reading and manipulation;
- **Text analysis** notebook: analysis of most common words, link with other quantities/factors, gathering of relevant insights.

## Installation and use
You can use the project's code by cloning it and making a local copy of it, open the _jobs_ads_scraping_ notebook and modify the URL of your research depending on the kind of search and job board you are interested in. Each job board is structured in its own way, so it is likely that you might have to change the way information is extracted from the scraped pages, by changing the loop within the _Loop acquiring job description, salary, location, type of contract_ section of the notebook.  
The saved job ads dataset can then be used in the _jobs_ads_nlp_ notebook. You can easily customize your analysis by selecting the key words you are most interested in, by including them in the _key_skills_ list of words. 
All of the key-words based analysis is easily customisable.

**OR** you could use Binder, by clicking on [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/RaffaToSpace/Job_ads_scraping_nlp/master)

## Project outcomes
This is an open-ended project and the outcomes can be continuously updated. The first version of the analysis is described in my Medium [post](https://towardsdatascience.com/how-to-identify-the-most-requested-skills-on-the-data-science-job-market-with-data-science-726845ca9638), as specified earlier. Otherwise you can go check the results dashboard page, on which I am going to post my findings as they come.

![wordcloud][wordcloud]

[wordcloud]: https://github.com/RaffaToSpace/Job_ads_scraping_nlp/blob/master/data/white_wordcloud4.png "Word Cloud"

