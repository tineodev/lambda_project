import json
import os
import mercadopago

def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])
    products = json.loads(event["body"])
    
    preference_data = {
        
        "transaction_amount": products["transaction_amount"],
        "token": products["token"],
        "installments": products["installments"],
            
        "payment_method_id": products["payment_method_id"],
        "payer": {
            "email": products["payer"]["email"],
            "identification": {
                "type": products["payer"]["identification"]["type"],
                "number": products["payer"]["identification"]["number"]
                }
            }
    }

    preference_response = sdk.payment().create(preference_data)
    
    return {
        "statusCode":200,
        "body": json.dumps({
            "name": preference_response["response"]["card"]["cardholder"]["name"],
            "status": preference_response["response"]["status"],
            "id": preference_response["response"]["id"],
            "status_detail": preference_response["response"]["status_detail"],
        })
    }
