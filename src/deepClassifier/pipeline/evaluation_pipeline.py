from deepClassifier.config import ConfigurationManager
from deepClassifier.components import Evaluation
from deepClassifier import logger
STAGE = "Evaluation"
def main():
    try:
        logger.info("{} {} {}".format("="*20,STAGE,"="*20))
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()
        logger.info("{}{}{}".format("="*20,STAGE + " " + "COMPLETED","="*20))

    except Exception as e:
        logger.info("There is error in data ingestion stage : " + str(e))
        raise e
       



if __name__ == "__main__":
    main()