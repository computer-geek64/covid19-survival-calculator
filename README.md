# COVID-19 Survival Calculator

*[COVID-19 Global Hackathon](https://covid-global-hackathon.devpost.com/)*

### This calculator is a web application that allows users who have coronavirus (COVID-19) to calculate the probability of their survival. We devised a machine learning algorithm that can accurately predict this value, taking into account a wide variety of factors, including information such as pre-existing medical conditions and local population statistics.

---

## Technologies used in this project

<img src="assets/img/xgboost.png" alt="XGBoost" title="XGBoost" width="150px" height="150px"><img src="assets/img/django.png" alt="Django" title="Django" width="150px" height="150px"><img src="assets/img/postgresql.png" alt="PostgreSQL" title="PostgreSQL" width="150px" height="150px"><img src="assets/img/pandas.png" alt="Pandas" title="Pandas" width="150px" height="150px"><img src="assets/img/jinja.png" alt="Jinja" title="Jinja" width="150px" height="150px"><img src="assets/img/nokogiri.png" alt="Nokogiri" title="Nokogiri" width="150px" height="150px">

* **XGBoost**
  * Developed a gradient boosting machine learning algorithm to accurately predict coronavirus survival rate (ensembled with a LightGB model for 95% AUC)
* **LightGBM**
  * Developed a gradient boosted model with optimized hyperparameters to predict coronavirus survival (ensembled with an XGBoost  model for 95% AUC)
* **Django**
  * Created a custom REST API for the front-end to call for making predictions and storing user data
* **PostgreSQL**
  * Maintained a database to efficiently access and update the aggregated datasets with new user data and live COVID-19 updates
* **Pandas**
  * Ran data analysis on many online datasets to accumulate appropriate training data for our machine learning model
* **Jinja**
  * Utilized templating engine to efficiently produce a functional front-end
* **Nokogiri**
  * Web scraped COVID-19 status pages to download and form datasets

## Programming languages

<img src="assets/img/python.png" alt="Python" title="Python" width="150px" height="150px"><img src="assets/img/javascript.png" alt="JavaScript" title="JavaScript" width="150px" height="150px"><img src="assets/img/ruby.png" alt="Ruby" title="Ruby" width="150px" height="150px">

* **Python** (3.7.7)
  * Project's main programming language
  * Created the machine learning algorithm and back-end API
* **JavaScript**
  * Used for developing the front-end website, along with Jinja and HTML/CSS
* **Ruby**
  * Required for web scraping COVID-19 status pages for live data

## Online datasets

* [DataHub.io Worldwide Time Series](https://datahub.io/core/covid-19)
* [Worldometers.info US States Cases/Deaths](https://www.worldometers.info/coronavirus/country/us/)
* [Worldbank.org Worldwide Population Density](https://data.worldbank.org/indicator/en.pop.dnst)

## How it works

This calculator is meant for patients who have tested positive for coronavirus to calculate their chance of survival. It can also be used by doctors to determine which patients to treat first. 

When the user visits the website, the website provides the user with a form with several input fields that are needed for the prediction algorithm, including age, gender, days between symptom onset and hospitalization, travel to any high risk areas, and any pre-existing medical conditions. Once this form is submitted, the website collects this data, along with the user's public IP address, and sends the data to the back-end API's primary endpoint for prediction. The back-end then uses an external API to geolocate the user to a specific country and region. The user's country and region is then cross-referenced with the live mortality rate datasets and population density datasets. All of this data is saved into the PostgreSQL database to be later converted into a new, merged dataset for retraining the model. Finally, the data is inputted into the gradient boosting machine learning algorithm to formulate an accurate prediction of the probability of survival.

## Machine learning models used

All of these factors are used to train two machine learning models: an XGBoost model and a LightGBM model. Both models employ algorithms that use gradient boosting to make predictions. XGBoost starts with one model, calculates the loss function of that model, creates a new model with parameters that minimize this loss function through gradient descent, and then adds that model to an ensemble. LightGBM is similar, but runs slightly faster with the risk of increased overfitting based on leaf-wise splitting of decision trees. 

The results from both models are weighted according to their relative accuracy to produce a weighted average. Any medical condition the user selects is then accounted for by inputting this weighted average into a sigmoid function with different weights for different medical conditions. This adjusted average is then displayed to the user on the website. 

## Team

* **Ashish D'Souza** - [computer-geek64](https://github.com/computer-geek64)
* **Varun Lakshmanan** - [varunlakshmanan](https://github.com/varunlakshmanan)
* **Pranav Pusarla** - [PranavPusarla](https://github.com/PranavPusarla)
* **Sharath Palathingal** - [therealsharath](https://github.com/therealsharath)
