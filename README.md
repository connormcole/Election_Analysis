# Election_Analysis

## Project Overview
A Colorado Board of Elections employee, Tom, gave me the following tasks to analyze the results of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote. 

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.9, Visual Studio Code 1.62.3

## Summary
The analysis of the election shows that:
- The total number of votes cast was 369,711.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23% of the total votes, which was 85,213 votes.
  - Diana DeGette received 73.8% of the total votes, which was 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the total votes, which was 11,606 votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the total votes, which was 272,892 votes.

## Challenge Overview
After submitting the initial code, Tom wanted us to also provide a breakdown for each county in the election.

## Challenge Results
The breakdown for each county was:
- The total number of votes cast was 369,711.
- The counties were:
  - Jefferson
  - Denver
  - Arapahoe
- The county results were:
  - Jefferson county cast 10.5% of the total votes, which was 38,855 votes.
  - Denver county cast 82.8% of the total votes, which was 306,055 votes.
  - Arapahoe county cast 6.7% of the total votes, which was 24,801 votes.
- The county with the highest turnout was Denver county.
- The candidate results were:
  - Charles Casper Stockham received 23% of the total votes, which was 85,213 votes.
  - Diana DeGette received 73.8% of the total votes, which was 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the total votes, which was 11,606 votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the total votes, which was 272,892 votes.

![Election_Results](https://user-images.githubusercontent.com/92554586/142772417-966fc438-16f4-47b8-ac46-00b16258397a.png)

![Election_Results_Code](https://user-images.githubusercontent.com/92554586/142774747-a346ece0-6d01-4856-923c-c2be20517f13.png)

## Challenge Summary
This script can be used for any local United States election, with the only changes being the input data and output .txt file. It will filter through every unique candidate and county and write the outcome to an easily readable file.

To modify this for a national election, the vote totals for each state would need to be tabulated in addition to each county. Assuming the input data had a column containing which state the vote was cast in, you could use similar logic and reference the index in each row tied to the state value, and add it to the total state vote count within the 'for' loop looping through all the rows of input data. You could then find the turnout for each state by dividing the state's total votes cast by the total votes cast nationwide. The winner would still be determined by total votes cast for them, regardless of where it was cast.

The code could also be made to work for a statewide election - you would just need to tabulate the total votes cast in the state, as well as each county in the state, and then output the candidate who won. The county with the highest turnout would use the same logic as the submitted code, and the overall state turnout would divide the total votes cast by the overall state population.  

