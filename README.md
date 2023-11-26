# The-Forage-
Virtual Work experience tasks

Task 3 - Creating effective visuals. The CEO and CMO would like you to provide them with some analysis and visuals that would help answer their questions. These results will help with effective decision-making and assist in their expansion strategy. You have noticed that the data contains some returns to the store which are provided in negative quantities and there are unit prices that were input in error. You will need to perform the following steps to clean this data: 
   Create a check that the quantity should not be below 1 unit.
   Create a check that the Unit price should not be below $0. 

Question 1 - The CEO of the retail store is interested in viewing the time series of the revenue data for the year 2011 only. He would like to view granular data by looking into revenue for each month. The CEO is interested in viewing the seasonal trends and wants to dig deeper into why these trends occur. This analysis will be helpful for the CEO to forecast for the next year.

My process: 
   The first step is to import all the necessary libraries and read the Excel online retail data file. Next, I chose to have a look at the overall data, and see its size and rows. I chose to visualise the data to see where there might be null values. ![q1 heatmap 3](https://github.com/ik339/The-Forage-/assets/99621737/9210cf35-e2f5-4441-ab6c-e7175c705aae) firgure 1. 
   As seen in Figure 1 The Majority of null values were in the column titled 'CustomerID'. I chose to drop the CustomerID column as I decided that it wasn't necessary information for Question 1, consequently creating a new data frame to keep the original just in case. I checked the data again and this is what it looked like in Figure 2. 
   ![q1 heatmap 4](https://github.com/ik339/The-Forage-/assets/99621737/7592bc40-2771-4b4d-b4b1-a3924ff9916c)
I also dropped duplicate rows. I then created the checks that I was asked to do.
   I then started to tackle the issue of creating a revenue time-series plot. to get the revenue I needed to multiply the quantity and unit price columns. to be able to extract data from the year 2011 I needed to make sure the invoice date column was in date-time format. I chose to extract 2011 data into a new data frame for convenience. 
   #new column for the month.
   # groupby month + revenue.
   #convert series to a data frame.
   #plot the time-series graph.figure 3 
![q1 timeseries 2](https://github.com/ik339/The-Forage-/assets/99621737/d208c417-b6e9-493e-8b53-34c2f917c575) figure 3. 
