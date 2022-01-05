# READ ME

***We explain everything with details in our pdf which you can read in the github: https://github.com/MaximeK30/Projet_VV***

During this project, we worked in the following dataset : https://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29#

Through the project, we tried to solve the following problems indicate in the link above :
* Seven class classifications for each drug separately.
* Problem can be transformed to binary classification by union of part of classes into one new class. For example, "Never Used", "Used over a Decade Ago" form class "Non-user" and all other classes form class "User".
* The best binarization of classes for each attribute.
* Evaluation of risk to be drug consumer for each drug.


## **Hypothesis:**


During the preprocessing, we analyse some features and we noticed that some features are not going to interfer in our classifictaion model in order to predict the risk to be a drug consumer. This issue is due to a lack of data in our dataset such as for country, ethnicity,... Moreover, we saw that young people are likely to be drug consumer because they want to try eveything at least once and they seek new sensation. Finally, we also noticed that people who left school earlier or are in stressfull studies are likely to use drugs. 

## **Models:**

* We divided the drugs in three categories:
    * The Heroin pleiad (heroinPl) includes crack, cocaine, methadone, and heroin.
    * The Ecstasy pleiad (ecstasyPl) includes amphetamines, cannabis, cocaine, ketamine, LSD, magic mushrooms, legal highs, and ecstasy.
    * The Benzodiazepines pleiad (benzoPl) includes contains methadone, amphetamines, and cocaine.


* We choose the monthly usage of drug to consider these people as drug-users. We decided to use “month-based” because for us the use of drug a decade ago or a year ago by a person may only for a purpose of test then he is not a real drug consumer. If we kept them as users, it might compromise our classification.


* We check our hypothesis so for that we create correlation graph and as we said we were able to drop three features among them ountry and Ethnicity and the other was Extraversion.

* After that we tried to find the best algorithm thanks to the best precision for Ecstasy and the best F1-score for Heroin and Benzodiazepines *(we explain this point clearly in the PDF).*

* Once, we found the best three algorithms for each drugs to classify, we tried to fine_tune them thanks to a gridsearch and the algorithm hyperparameters. Sometimes the default parameters are better than what we received from the fine tunning algorithm composed by the gridsearch algorithm.

* Algorithm that we choosed after the fine-tuning for the flask model in the next part:
    * HeroinPl: NearestCentroid()
    * EcstasyPl: LogisticRegression(C=0.1, class_weight='balanced', solver='liblinear')
    * BenzoPl: NearestCentroid(shrink_threshold=0.0)

## **Flask:** *www.trademanager.fr:5000*

* Thanks to Dorian Velut's Raspberry, you are able to access to this flask every where and when ever you want just by clicking in the link above.

* Our flask allows some users to know if they are likely or not to be a drug user.

* The principle is simple :
    * We fill each features and we submit and then we received the percentage of a user to likely be a user for HeroinPl, EcstasyPl and BenzoPL.
    * Then we have the probability to be likely a user of drugs or not.
    * We must consider that the F1-score is not high thus we don’t have to have a blind trust according the benzoPL and heroinPl prediction because of the lack of data.
    
