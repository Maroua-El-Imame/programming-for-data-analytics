# Project : Windspeed Analysis 

Lecturer : Andrew Beatty  
Programming and Scripting S2-2025  
Higher Diploma in Science in Computing in Data Analytics  
Atlantic Technological University - ATU Galway Mayo 2025/2026.  

Author : Maroua EL imame  

Submission deadline : 12/01/2026  


<br/>
<br/>
<br/>
<br/>
<br/>




## Introduction  
<br/>


Wind energy is one of Ireland's most important renewable resources. Understanding wind patterns helps explore energy potential.  

Mace Head station is a particularly relevant case study, having received the highest number of wind warnings in Ireland since 2020.  
Over this period, Galway recorded 234 wind warnings, spanning 66 days and 1,603 hours, with maximum wind speeds reaching 145 km/h, highlighting the county’s exposure to frequent and intense wind events.  

The Map Alerter [*article*](https://www.mapalerter.ie/blog/met-eireann-severe-weather-galway-wind-2025) "*Storm Events and Maximum Wind Speeds*" , supports the selection of Galway as the primary study location, demonstrating:  

High frequency of wind events  
Exposure to severe wind conditions  
Relevance for wind energy discussions  

Given my residence in Galway, this study is of particular interest, providing a local perspective on wind energy potential.  

This project examines historical wind data for Mace Head station to identify trends over time, including daily, monthly and seasonal variations, it also explores simple predictions of future wind patterns.  

The methods used in this project can be extended in future work to compare multiple locations across western Ireland or to incorporate more advanced predictive models.  
<br/>

## Project workflow
<br/>



The following workflow outlines the step-by-step process of this project based on the Data Science/Analytics project lifecycle.  

Each step will be addressed in the notebook, with outputs, analysis and commentary as the project progresses:  

- [✔️] **Problem Definition**   
    Define the project goal/scope of analyzing windspeed at Mace Head.    
- [✔️] **Data Collection**  
    Gather historical windspeed data.   
- [✔️] **Data Preparation**  
    Handle datasets inconsistencies.
- [✔️] **Exploratory Data Analysis**  
    Visualize wind speed trends and patterns.   
- [✔️] **Modeling and Evaluation**  
    Estimate potential turbine power, analyze trends and predict future wind patterns.  
- [✔️] **Documentation and Reporting**  
    Record findings, plots and interpretation.  

<br/>

## Data Source  
<br/>

The Irish Meteorological Service ***[Met Éireann](https://www.met.ie/climate/available-data/historical-data).*** 
<br/>

## Analysis approach  
<br/>


I followed a standard data science workflow from raw data to actionable insights with a focus on wind energy relevance at each step:

1- Problem definition and listing of research questions  
I started with real world qurstions : Is Mace Head windy enough ? Are winds changing over time?   

2-Data collection: 22 years of hourly windspeed records  
I used Met Éireann's historical dataset (2003-2025), giving enough data for both seasonal patterns and long term trend analysis.   

3-Data preparation through cleaning and resampling  
I handled missing values, converted units ( knots into m/s for energy calculations) and created daily/monthly/yearly and seasonal views for different analysis scales.    

4-Exploratory analysis  
I pplied rolling averages, seasonal analysis, heatmpas etc. to answer when and how wind varies at Mace Head.  

5-Modeling and Evaluation  
I worked on trend analysis with linear regression to quantify wind fuctuations, I also used ARIMA forecasting for short term windspeed predictions, and Turbine treshold mapping to assess opearional feasibility.   

6-Documentation    
I used clear visualizations ( wind vs temperature Plots, threshold Scatter plots, Heatmaps, Barplot, Diagnostics ..).  added clear, detailed  comments in section of code where they're relevant and also markdwon explanations to make the finding easy to understand to both technical and non technical readers.  

## Conclusion 
<br/>

This project has successfully transformed 22 years of hourly wind observations from Mace Head station into a comprehensive assessment of wind energy potential.   
It shows how accessible meteorological data, when analyzed with a clear question driven workflow, can bridge the gap between historical weather records and informed decision for a sustainable energy future.  

Data cleaning, multi scale windspeed analysis and practical energy calculations have answered the core of research questions.  

Seasonal and daily patterns are clearly established with winter winds consistently strong in Winter and the calmest in Summer, following predictable annual cycles.  
Wind turbine suitability is confirmed with approximately 80 % of hourly wind speeds falling within operational ranges with rare extreme events.  
Long term trends reveal gradual but stastically decline in wind speeds of approximately 0.24 knots per decade.  






## Environment Setup :
<br/>

| Python in repository - File browsing & viewing     |
|----------|


-Access the repository: You're already viewing the main [repository](https://github.com/Maroua-El-Imame/programming-for-data-analytics/blob/main/project/README.md) 
page.  
-View python file types: .py or .ipynb .  
-Navigate folder using the file explorer on the left. 
-Click on ipynb files to see their content, code and code output.  
-Notebook ouputs display automatically if no installation is planned.     



| Python in Git     |
|----------|


-Navigate to github  
-Click Sign up  
-Follow the prompts to create a personal account.  
***  
-Go to github.  
-Log in to your account.  
-Click the new repository button in the top-right **'+'** symbol   
-Follow [steps](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)  
-Click create repository.  
***  
-On GitHub, navigate to the main page of the repository.  
-Under the repository name, select the code dropdown menu.  
-Click Create codespace on main.  
-From menu top left click on View > Explorer -  
-Under repository title (in bold) click on New file  
-Lower case file name, then add .ipynb extension ( for notebook format) or .py extension ( for python file).  
-Follow steps from developing a code to committing then lastly syncing changes.


| Python on Windows     |
|----------|


[Download cmder](https://cmder.app/)  
[Download notepad++](https://notepad-plus-plus.org/)  
[Download anaconda (python)](https://www.anaconda.com/download)   
[Download vs code](https://code.visualstudio.com/Download)  


*** 
-Open VS Code and select "File > New File",  
    Save the file as .py format (e.g., my_script.py).  
    Write a Python script in the file.  


-With Python file open in VS Code, launch the terminal (see vscode menu)  
    Navigate through the terminal until reaching the same directory where Python file is located.  
    Possible to use Cmder for running Python code (CAT). Same as in Vs code, navigate to the directory where the Python file is 
saved using the cd command.  


-Cmder is mainly for command-line usage, while VS Code is where would most of coding and debugging run.   


-Lastly, steps to [clone repository using command line](https://docs.github.com/en/repositoriescreating-and-managing-repositories/cloning-a-repository)  
    Clone allows to copy the repository from GitHub to the local machine  
    Changes can be pushed to the remote repository on GitHub and/or pulled from Github into the local machine.  

## Contact  
<br/>

Maroua El imame   
Author and sole contributor   
G00472980@atu.ie   
