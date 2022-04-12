FROM quay.io/ml-aml-workshop/python:3.7-slimv2

WORKDIR /microservice
COPY requirements.txt /microservice/
RUN pip install -r requirements.txt
RUN pip install seldon-core==1.12.0
RUN pip install joblib
RUN pip install category_encoders==2.2.2
RUN pip install dill
RUN pip install MarkupSafe==2.0.1

COPY Predictor.py  Transformer.py model.pkl CustomerChurnOrdinalEncoder.pkl CustomerChurnOneHotEncoder.pkl /microservice/

ENV PERSISTENCE 0
CMD seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE --persistence $PERSISTENCE --grpc-port ${GRPC_PORT} --metrics-port ${METRICS_PORT} --http-port ${HTTP_PORT}

# FROM registry.access.redhat.com/ubi8/python-38

# WORKDIR /microservice
# RUN pip install alibi_detect
# RUN pip install seldon-core
# RUN pip install joblib
# RUN pip install scikit-learn
# RUN pip install category_encoders
# RUN pip install dill
# USER root
# RUN dnf install -y mesa-libGL
# USER 1001
# # ADD CustomerChurnDriftPredictor /microservice/CustomerChurnDriftPredictor
# COPY Predictor.py model.pkl Transformer.py  /microservice/
# ENV PERSISTENCE 0
# CMD seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE --persistence $PERSISTENCE --grpc-port ${GRPC_PORT} --metrics-port ${METRICS_PORT} --http-port ${HTTP_PORT}