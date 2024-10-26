# US-Visa-Approval-Prediction
## (MLOps)

## Docs & Links

[link] www.google.com/Us-visa-approval-prediction:
#### (Git-commands)

```bash

Set up a git Repo: "US-Visa-Approval-Prediction"

Make a folder in local system then navigate to it using cd in git bash 

Then execute this command: 

git clone https://github.com/Bhomitkapoor/US-Visa-Approval-Prediction.git

cd US-Visa-Approval-Prediction





# how to commit 

git add . 

git commit -m "folder structure added"

git push origin main


```

conda create -n visa python=3.8 -y

-e .    "in req.txt"  is responsible for setup.py
How to run?
conda create -n visa python=3.8 -y
conda activate visa
pip install -r requirements.txt


### Mongo-dB Setup

![alt text](image.png)
Create a MongoDB Project: us-visa-project

[Link]  https://cloud.mongodb.com/v2/65d8b164318246702fbc99b8#/overview

Create a cluster with MongoDB 
![alt text](image-1.png)


IP Address   :   to connect with any other system we need this IP address configuration.
![alt text](image-3.png)   

## successful setup of MongoDB 

![alt text](image-4.png)



click on connect button: 
![alt text](image-5.png)

![alt text](image-6.png)

Take the connection String and copy it.


### Create a Notebook in Notebooks folder and then paste the connection string into the notebook.


once you have your data in the MongoDB : 
![alt text](image-7.png)







https://www.kaggle.com/datasets/moro23/easyvisa-dataset 



# utilis -> the common functionwe use 




#######################################################################################################

Workflow 
1.) constant   (define constants)
2.) config_entity    (all the folder & file path)
3.) artifact entity     (all the output files to be generated)
4.) component   (data ingestion & other stages like transformation, validation, etc)
5.) pipeline    
6.) app.py






#####################################################################

HOW TO EXECUTE THIS 

Open Git BASH navigate to the directory
Activate venv : conda activate visa

then excute the following commands as it contain the mongodbURI , it will be different for your mongodb but u need it ;) hehe :)
  export MONGODB_URL="mongodb+srv://bhomitsopra:lDsBZ63S0f9QvWf4@cluster0.yagn7o9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
  python demo.py



#####################################################################
very first file in project has to be the COnfig file  -> Constants -> _init_.py file. this is our constructor file also.

DATA INGESTION  ----> DATA VALIDATION...

1.) Data Validatiion Component  : In data validation we check the columns then we do the datat drift checking if the status of datadrift is false in report. then we proceed with next.   
    It only returns True Falase that tells whether the data is valid or not for next components or step.  The distribution of data has to good and reshuffling helps in achieveing it.

    schema.yaml -  we prepare it for describing the columns how to deal with them in the dataset
    This file schema.yaml has to read by the read_yaml function present in main_utils.py file.

        **  (config_entity.py & artifact.py has to be added with the details)  **

        ** Inside the dataValidaiton class detect_dataset_drift is responsible for returning the train - test drift results true false there we have the reference_df means the traiing datat and current_df means the test data the new data where we want to check.



2.) Data Transformation Component : 



3.) Model Trainer



4.) Model Evaluation


5.) Model Pusher


6.) Prediction Pipeline


7.) Deployment