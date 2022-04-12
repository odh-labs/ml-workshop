def get_params():
    # ##########################################################################
    #
    # PLACE YOUR STUDENT CONFIGURATION INFORMATION IN THIS SECTION OF THE CODE
    #
    user_id = "user123"
    # minioFilename = "your.csv"
    # ##########################################################################
    
    # ##########################################################################    
    #
    # DO NOT CHANGE ANY CODE BELOW THIS LINE
    #
    # ##########################################################################
    PROJECT_NAME = "CustomerChurn-"+user_id
    EXPERIMENT_NAME = PROJECT_NAME
    experiment_name = EXPERIMENT_NAME.lower()
    # s3BucketFullPath = "full_data_csv-"+user_id+"/"+minioFilename
    s3BucketFullPath = "full_data_csv-" + user_id

    print("STUDENT CONFIGURATION")
    print("=====================")
    print(f"User ID: \"{user_id}\"")
    print(f"Project name: \"{PROJECT_NAME}\"")
    print(f"Experiment name: \"{EXPERIMENT_NAME}\", \"{experiment_name}\"")
    print(f"S3 Bucket full storage path: \"{s3BucketFullPath}\"")

    return user_id, PROJECT_NAME, EXPERIMENT_NAME, experiment_name, s3BucketFullPath


def download_csv_files(minio_client, s3_folder_path):
    # not tested code
    # it will get all the files from the user bucket
    csv_files = minio_client.list_objects("data", recursive=True, prefix=f"/{s3_folder_path}")
    for csv_object in csv_files:
        print(csv_object)
        csv_object_name = csv_object.object_name
        if csv_object_name.endswith('csv'):
            # minioClient.fget_object('data', csv_object_name, csv_object_name.split("/")[-1])
            minio_client.fget_object('data', csv_object_name, "/tmp/data.csv")
