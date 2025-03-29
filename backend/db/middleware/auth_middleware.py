from fastapi import Cookie, HTTPException
from secret_keys import SecretKeys
import boto3

secret_keys = SecretKeys()
COGNITO_CLIENT_ID = secret_keys.COGNITO_CLIENT_ID
COGNITO_CLIENT_SECRET = secret_keys.COGNITO_CLIENT_SECRET
REGION_NAME = secret_keys.REGION_NAME
cognito_client = boto3.client("cognito-idp", region_name=REGION_NAME)


def _get_user_from_cognito(access_token: str):
    try:
        user_res = cognito_client.get_user(AccessToken=access_token)

        return {
            attr["Name"]: attr["Value"] for attr in user_res.get("UserAttributes", [])
        }
        return user_res
    except Exception as e:
        raise HTTPException(500, "error fetching user")


def get_current_user(access_token: str = Cookie(None)):
    if not access_token:
        raise HTTPException(401, "User not logged in!")

    return _get_user_from_cognito(access_token)
