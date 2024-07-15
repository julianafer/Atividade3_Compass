import boto3
import joblib
import os

from dotenv import load_dotenv

# loads environment variables
load_dotenv()


class ModelLoader:
    bucket_name = os.getenv('BUCKET_NAME')
    model_key = os.getenv('MODEL_KEY')

    def __init__(self):
        self.model = None
    
    def load_model(self):
        local_model_path = 'model.tar.gz'
        extracted_model_path = 'xgboost-model'
        model_file = os.path.join(extracted_model_path, 'xgboost-model')
        
        # Check if the model file already exists
        if os.path.exists(model_file):
           print("modelo encontrado")
        else:
            # Create a session using boto3 with the specified AWS profile
            session = boto3.Session(profile_name=PROFILE_NAME)
            s3 = session.client('s3')  # Create an S3 client using the session
            
            try:
                s3.download_file(BUCKET_NAME, MODEL_KEY, local_model_path)  # Download model archive from S3 to local path
                logger.info(f"Modelo baixado para: {local_model_path}") 
                
                if not os.path.exists(extracted_model_path):
                    os.makedirs(extracted_model_path)  # Create directory if it doesn't exist
                
                with tarfile.open(local_model_path, 'r:gz') as tar:
                    tar.extractall(path=extracted_model_path)  # Extract model files from the tar archive
                
                extracted_files = os.listdir(extracted_model_path)  # List extracted files from the directory
                logger.info(f"Arquivos extraídos: {extracted_files}") 
                
                if not os.path.exists(model_file):  # Check if the model file exists after extraction
                    logger.error(f"Modelo não encontrado em: {model_file}")  
                    return None
                
            except Exception as e:
                logger.error(f"Falha ao carregar o modelo do S3: {str(e)}")  
                return None

        model = xgb.Booster()  # Create an instance of XGBoost Booster
        model.load_model(model_file)  # Load the model from the specified model file
        logger.info("Modelo carregado com sucesso.") 
    
    return model  # Return the loaded XGBoost model
    
    def predict(self, data):
        if self.model is None:
            raise Exception("Model is not loaded")
        return self.model.predict(data)
