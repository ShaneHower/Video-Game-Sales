# Video-Game-Sales
An Analysis of Video Game Sales 

## Describe the Data
I first looked for data sets online.  My search lead me to a website called Kaggle.  Kaggle is an open forum for all things data.  Members post their recent projects and data can be found and downloaded on almost any subject.  I found a data set that had video game sales and ratings from 1985-2017.  I used this data set to learn more about coding in python and how to write queries for large data sets.  My first objective was to import the data into pandas (a python library that allows you to work with data sets) and get some key information from it.  One issue that I ran into was that some columns had null values (or an empty entry).  If I wanted to do anything meaningful with the data, I had to delete these nodes.  I originally used a dropna() command (which takes out any row that has a null value) to my data set, however, this would take out entire rows where there was still valuable information. For example, if I took out any row with a null entry in the column “Critic Score” I could be losing rows that have data in “Global Sales”.  Having this discrepancy would give a less accurate description of the units sold, which I will I will analyse later.
Instead of using the dropna() command I inputted a 0 for any node that had a null value. By doing this I could still perform mathematical calculations with the empty entry.  After taking care of the null values in the set I wrote a simple query that would display a table.  This table would show measurements such as mean, standard deviation, and quartiles.  The command to complete this task is .describe().  I restricted my data set so I would only get this information from the sales columns.  These were my results:  

![screen shot 2017-10-30 at 9 27 25 pm](https://user-images.githubusercontent.com/34482822/34427833-5902c068-ec14-11e7-94ca-1be3f91c65f1.png)

## Grouping Sales by Genre
This information is good to know, but it doesn’t tell us anything interesting about the data.  Perhaps we can find some useful information if we could compare the number of sales between genres.  What genre seems to have the most popularity over the past few decades? To find this out, I had to group the data by genre and restrict the set to just global sales.  The idea behind solving this problem is to construct an empty data set and assign only the columns in which I was interested into the new table.  Grouping the data by genre allowed me to calculate the sum of each genre’s global sales.  It also allowed me to make a new column called ‘count’ which counted how many games were in each genre.  

![screen shot 2017-10-30 at 9 38 14 pm](https://user-images.githubusercontent.com/34482822/34427862-a1b09f24-ec14-11e7-936c-b047e8277edb.png)

## Constructing a Bar Graph
Now I have a readable table of all the genres and how much money was made from each over the 31 year span.  This is very useful information to know.  Perhaps I’m a video game developer, and I want to optimize the success of a video game I’m about to put into development.  Knowing what type of game is historically more popular can help me make educated decisions in developing the game.  This table is helpful, but we can format the data so it is easier to read by representing it as a bar graph.  

![global sales by genre](https://user-images.githubusercontent.com/34482822/34427873-c824b4ba-ec14-11e7-9cce-afcc79d9bcc5.png)

## Sales of Genres by Year

As we can see the ‘Action’ genre seems to sell the most.  The most difficult part of making this bar graph was getting the genres on the y axis in a neat manner.  In order to construct this bar graph I used the python library Matplotlib. The challenge that arose from working with Matplotlib was that the bar graph function required numbers on the x and y axes.  The genres are a class type called a string (a word or letter) so I had to find a specific command (yticks()) which sets the location and labels of the axis. After successfully getting these labels on the correct axis, they were all jumbled together and the titles were being cut off.  The command plt.tight_layout() cleans up the graph so that it looks organized and easily readable. 
I know the global popularity of each game genre from 1985 to 2017, but what if I want to know how each genre fared year by year?  The first step in learning this information was to once again group the data.  Before grouping I wanted to restrict my data set so that I was just viewing the sales from 2015 and 2016.  After restricting the set I grouped my data by the “Year_of_Release” column as well as the “Genre” column and plugged it into an empty data set.  


![screen shot 2017-10-31 at 2 24 21 pm](https://user-images.githubusercontent.com/34482822/34427884-f9bb13c0-ec14-11e7-968a-99826c26428d.png)

## Consrtructing Pair Plots
The last concept I was able to learn was constructing pair plots and heatmaps.  These show how the variables in the set correlate to one another.  A pair plot shows each data plotted on an xy plane in relation to another variable.  A heat map assigns a value and a color to the relationship between two variables in reference to their correlation.  A variable relationship is much easier to read in the heat map but there is more information in the pair plot.  

![pairplot](https://user-images.githubusercontent.com/34482822/34427900-22a7b78e-ec15-11e7-9428-70f3a0a59cc9.png)

## Heat Maps
On the chart above each dot represents a piece of data.  For instance if we look at the graph in the bottom left corner it compares the critic score (x axis) to Japan’s sales (y axis).  Let’s take a look at the game Wii Sports:

![screen shot 2017-12-28 at 9 31 02 pm](https://user-images.githubusercontent.com/34482822/34428039-81ed5086-ec16-11e7-99e0-cde282903260.png)
For this specific example we would graph Wii Sports in the bottom left corner at (76.0,3.77).  Plotting all of these points will reveal if two variables have a positive, negative or no correlation.  A heat map will read the correlation between two variables and assign it a value.  The higher the value the greater the correlation between two numbers. 

![heat map](https://user-images.githubusercontent.com/34482822/34428053-9fdd128e-ec16-11e7-819a-83eecd943818.png)

Data used from: https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings/data