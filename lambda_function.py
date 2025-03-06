# Imports
import boto3
import json


# Função lambda
def lambda_handler(event, context):
    # Cria o cliente SageMaker
    runtime_client = boto3.client("runtime.sagemaker")

    # Nome do endpoint
    endpoint_name = "sagemaker-xgboost-2025-03-06-20-52-42-958"

    # Variáveis de entrada
    x1 = event["x1"]
    x2 = event["x2"]
    x3 = event["x3"]
    x4 = event["x4"]

    # Cria a amostra de dados
    sample = "{},{},{},{}".format(x1, x2, x3, x4)

    # Invoka o endpoint, passando a amostra como entrada para receber como resposta a previsão
    response = runtime_client.invoke_endpoint(
        EndpointName=endpoint_name, ContentType="text/csv", Body=sample
    )

    # Formata a resposta
    result = int(float(response["Body"].read().decode("ascii")))

    print(result)

    # Retorno
    return {"statusCode": 200, "body": json.dumps({"Prediction": result})}
