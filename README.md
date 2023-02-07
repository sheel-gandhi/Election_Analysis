# Election_Analysis
Election Analysis using Python

## Overview of Election Audit

Tom, a Colorado Board of Elections employee needs our help with auditing and analysing the tabulated elections results for a US Congressional Election in a precinct in Colorado. The purpose of the Audit will be to get the total number of votes cast, votes cast in each county and its percentage in total votes, and number of votes for each candidate and its percentage in total votes. At the end, we will be able to determine county with maximum number of votes and candidate with maximum number of votes with its votes and percentage. 

Considering the large amount of data in hand, we will be using Python and its automated process to achieve our outcomes. A successful Python process going forward can also help in auditing Senatorial Districts Elections and Local Elections. 

Software Used: Python, Visual Studio Code

## Election-Audit Results

***Total number of votes cast in congressional election***
                    
   * Total votes cast in the congressional election is `369,711`.

***Breakdown of the number of votes and the percentage of total votes for each county in the precinct***

   * Jefferson County has a total of `38,855` votes which is `10.5%` of the total vote count. 
   * Denver County has `306,055` votes which is `82.8%` of the total vote count.
   * Arapahoe County has `24,801` votes which is `6.7%` of the total vote count.
  

***County with the largest number of votes***
  
  * `Denver` County is the Largest County.
  * Denver County has the largest number of votes with `306,055` votes.
  * Denver County has the largest vote percentage at `82.8%`.
   

***Breakdown of the number of votes and the percentage of the total votes each candidate received***

  * Charles Casper Stockham received a total of `85,213` votes which is `23.0%` of total votes.
  * Diana DeGette received `272,892` votes which is `73.8%` of total votes.
  * Raymon Anthony Doane received `11,606` votes which is `3.1%` of total vote count.


***Winning Candidate, their vote count, and their percentage of the total votes***

  * `Diana DeGette` is the winning candidate
  * Diana DeGette received highest number of votes with `272,892` votes.  
  * She received `73.8%` of the total votes cast. 

## Election-Audit Results Method

***Total number of votes cast in congressional election***
          
The election results csv provided will be opened and read and we shall be removing the header so that the header is not counted towards analysis. We will be initializing  Total Votes with 0 and with the help of the following code, count the total votes cast in the election. In the code, we are looping through each row in our csv file to count the votes.

![total_votes_code](https://user-images.githubusercontent.com/108366412/180130269-fee61508-bb57-424c-99a6-e52f6fa87fa4.png)

***Breakdown of the number of votes and the percentage of total votes for each county in the precinct***
 
To extract this information, first we will be pulling the list of counties from our database with a loop and append command- (county_list.append(county_name)). Then we will initialize each county’s vote count with 0 and with a new loop, we will extract information on the number of votes cast for each county.  Based on the total votes and county votes, we can get percentages for each county. The below screenshot gives a clear view of the code to achieve the above outcomes.
 
![county_votes_percentage](https://user-images.githubusercontent.com/108366412/180150018-22da8364-32da-4a0e-b9c0-9793dd35b657.png)

![county_results](https://user-images.githubusercontent.com/108366412/180150030-8f19524b-ee84-45af-b72e-aac8655c7015.png)


***County with the largest number of votes***

To determine the largest county, first we will initialize a variable called “largest_ county_voter” and set it to 0 and then comparing each county votes with the largest_county_voter variable, we will get the county with the maximum number of votes. Below screenshot will give a better understanding of the if-then condition. 

![winning _county](https://user-images.githubusercontent.com/108366412/180150074-1417f519-1caf-42e5-bb1a-64fa266aa600.png)
 
***Breakdown of the number of votes and the percentage of the total votes each candidate received***

We shall be first looping through the data to find the list of candidates standing in the election. For this, we will use append command - (candidate_options.append(candidate_name)). Then, after initializing the number of votes for each candidate to 0, with a new loop, we will get the number of votes that each candidate received. The percentages of votes each candidate received will then be calculated with the total votes and candidates votes information. 
 
![candidate_votes_percentage](https://user-images.githubusercontent.com/108366412/180150166-a3ec43c4-8dbc-465e-acc7-9cad9c9c14d5.png)

![candidate_results](https://user-images.githubusercontent.com/108366412/180150188-d26d6a3c-dda8-458c-a239-6c556eb77ae3.png)

 
***Winning candidate, their vote count, and their percentage of the total votes***

To find the winning candidate, first we will initialize a variable called “winning_count” and set it to 0 and then comparing each candidates vote count with the winning_count variable, we will get the candidate with the maximum number of votes. Below screenshot will give a better understanding of the if-then condition. 

![winning_candidate](https://user-images.githubusercontent.com/108366412/180150221-2671ec2f-b24b-401d-8c82-bef34788401e.png)

## Election-Audit Summary

The results achieved from running Python code provides brief outlook of the election audit. It provided total votes, county votes, candidate votes and percentages which also helped in determining winning candidate and largest county. This automated process can certainly assist in many large election audits such as a Senatorial Elections or even a Local Elections. 

To make the code’s usage more diverse, we can add the following results to the existing outcomes

  * Number of votes each candidate received in a particular county. This will help in determining if there is a dominance of a particular candidate in that county even though that candidate is not the overall winner of the election.
  * In the dataset, new columns can be added like Demographic information on voters and audit can be ran on Gender, Profession, and Income. For the new columns we can find each candidate votes and each county votes.
