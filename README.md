# Women-Force labor rate-predication-and-deployment-by-flask
This project is used for Predicating Women Force Labor rate based on different features of Data. These features of data are is country a european member, is country developed, enterpenership index, inflation rate of country. Multiple Linear regression is used for data trainnig and predication. 
# step 1 Data collection
Data is available on kaggle website and collected from there.
# step 2: Work on jupter notebook
# importing Data set
First of all imported data set in the project for that purpose use pandas library and save data in data frame.
# Checking null values
First of all check null values and there are no null values in data. After this convert numerical object data into float data type by using lambda
# Visualization
Then visulize data and understand it by matplotlib and seaborns
# outlier
In next step check for outliers in data and remove it.An outlier is a data point in a data set that is distant from all other observations.
# dummy variables for categorical data
Then use dummy variables for categorical data and convert it to 0 and 1.
# remove variable with high coorelaetion with each other
After this we check and remove variable with high coorelaetion. For that purpose use the function of df.corr()and seborn for analyssi of correlation.
# train test split 
 Firt convert data into X and y variable.In next step split data into testing and training data by train test split.
 # Modeling
For predication use linear regression and predicated force labor rate.
# Save the model
Then use pickle to save model
# Flask
import same model in flask and apply all the step that are performed in above use case
# # index.html
At end render index.html
index.html is placed in templates folder

