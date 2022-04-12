def get_hyper_paras():
    # ##########################################################################
    #
    # PLACE YOUR STUDENT CONFIGURATION INFORMATION IN THIS SECTION OF THE CODE
    #
    user_id = "user123"
    minioFilename = "your.csv"
    # ##########################################################################
    
    # ##########################################################################    
    #
    # DO NOT CHANGE ANY CODE BELOW THIS LINE
    #
    # ##########################################################################
    PROJECT_NAME = "CustomerChurn-"+user_id
    EXPERIMENT_NAME = PROJECT_NAME
    experiment_name = EXPERIMENT_NAME.lower()
    s3BucketFullPath = "full_data_csv-"+user_id+"/"+minioFilename

    print("STUDENT CONFIGURATION")
    print("=====================")
    print(f"User ID: \"{user_id}\"")
    print(f"Project name: \"{PROJECT_NAME}\"")
    print(f"Experiment name: \"{EXPERIMENT_NAME}\", \"{experiment_name}\"")
    print(f"S3 Bucket full storage path: \"{s3BucketFullPath}\"")

    return user_id, PROJECT_NAME, EXPERIMENT_NAME, experiment_name, s3BucketFullPath
