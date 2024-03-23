from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize the Kaggle API
api = KaggleApi()
api.authenticate()

# Tokyo Olympics Datasets Download

dataset_name = "arjunprasadsarkhel/2021-olympics-in-tokyo"
api.dataset_download_files(dataset_name, 
                           path='./datasets/', 
                           unzip=True)