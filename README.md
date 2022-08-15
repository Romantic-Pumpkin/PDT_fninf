# About PDT_fninf
In order to accelerate progress in cohort studies, we proposed a hierarchical neuroscience knowledge base consisting of projects/organizations, multi-modal databases and toolkits, and take the information object in Frontiers in Neuroscience as a example input. Meanwhile, we developed and open sourced the query tool, PDT_fninf , so that researchers can quickly access the knowledge base, as shown in below figure. 

![image](https://user-images.githubusercontent.com/30644650/184585532-1521c51a-f497-45e0-a5f6-54913343abcd.png)


# How to use it 
  ##Step1: Download and unzip the Github repository to your local or server;
   1. git clone https://github.com/Romantic-Pumpkin/PDT_fninf.git
   2. tar xzvf PDT_fninf.tar.gz your local path/PDT_fninf
  
  ##Step2：Start the flask-based API service;
   1. python pdt_fninf_web.py
   2. demo: find access the Google Chrome in https://127.0.0.1:8080/index
  
  ##Step3：Select the information object category within ["Projects","Databases","Tooklkits"];
  
  ##Step4：Input the corresponding keywords like "neuroimaging;austim";
  
  ##Step5：Press Enter to retrieve the content your need.
