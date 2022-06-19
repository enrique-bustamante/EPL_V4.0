# English Premier League Algorithm V4

## Purpose

The purpose of this project is to determine the best players to select for the
English Premier Fantasy League using data analysis and visualization. Factors
such as a players cost, points, form, and others will be taken into consideration.


## Methodology

### Tools
* Python
* HTML
* CSS


### Packages
* Pandas
* Scikit Learn
* Flask
* Seaborn
* Matplotlib
* requests
* Beautiful Soup
* Dataframe Image
* Pyscript (eventually)

### Version
* 4.0 - Copied V3.0 and added in dream team along with automatic calculation of minutes cutoff

### Custom functions

I imported custom functions that I created for use in this project. They are
included in the myFunctions.py document and imported into the webscraping
script.

Here are the functions I created:

__columnsAsType:__ This takes a dataframe, the list of columns to be
converted, and the type you want to change them to en masse. The output
is the dataframe with the converted dataypes.

__positionDf:__ This function takes a dataframe and the position as an
input. Since the main dataframe is broken out into positional dataframes,
this functions made it convenient to do so with less code.

__rankDf:__ This functions takes in a dataframe, the column name to be
created, and the column being ranked. This first ranks the dataframe by
the specified column and a new column is created displaying the ranks.
The column is then sorted by rank in descending order.

__zScore:__ This function takes in a dataframe, finds the means and standard
deviations of the vlue, projection, form, and total points. These were
then used to find the z-score for all of the specified columns for
ranking and final projection.


## Webscraping Script

### API scraping

Using an api, a JSON containing the EPL data is downloaded into a few pandas
dataframes. The teams and positions are of separate dictionaries in the JSON so
pandas merge was used to combine all into one dataframe after the data has been
cleaned.

### Data cleaning

First I set the ID from the elementsDf dataframe to be the index. Then, I joined
the positions from the elementTypesDf dataframe as the positions column in our cleaned dataframe.
Next, the team from teamsDf was mapped to be added to the elementsDf dataframe.

Next, for some reason, the cost of the players is multiplied by 10 so I divided
the 'now_cost' from the original data by 10 to corrrect this. To calculate
value, the 'total_points' column was divided by the correct 'now_cost' column.

Then, I converted the 'form', 'points_per_game', and 'ict_index' columns to a
float using the columnsAsType function. I then reduced the dataframe to
essential columns and set the index to 'web_name'.

Lastly, I created an input box to get the gameweek and multiply it by 60 to
represent the minimum points needed to get 2 points in the Fantasy Premier
League. I filtered out all players that do not meet this minimum minute mark to
avoid players that have one good game every so often but don't play real
minutes.

### Machine Learning

These are the steps I followed
1. I separated the dataframes into categorical and numerical dataframes.
2. The numerical dataframe was then separated into attributes and features to run through our ML model.
3. These were then split into test and training sets using train_test_split.
4. The numerical attributes were standardized using StandardScaler.
5. The model was finetuned using GridSearchCV to determine the best number of estimators.
6. The estimator was then plugged into the RandomForestRegressor as a parameter and the model was fit to the training data
7. The test set was then used to predict the projections for points.
8. The entire set was then passed through the model to get the final projections

### Statistics




## Visuals
![](images/form.png)
