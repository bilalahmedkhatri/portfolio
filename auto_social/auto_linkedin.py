import os, sys
from dotenv import load_dotenv, find_dotenv
from linkedin_api.clients.restli import client

dir = sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(find_dotenv())

LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")

print("type : ", type(LINKEDIN_ACCESS_TOKEN))

if LINKEDIN_ACCESS_TOKEN is None:
    raise "please provide linkedin credential!"

PROFILE_SOURCE = "/me"

restli_client = client.RestliClient()

# res = restli_client.get(
#     resource_path=PROFILE_SOURCE,
#     access_token=LINKEDIN_ACCESS_TOKEN,
#     query_params={"fields": "id,firstName:(localized),lastName"},
#     )

# print("results", res.entity)

response = restli_client.get(
    resource_path=PROFILE_SOURCE,
    access_token=LINKEDIN_ACCESS_TOKEN,
    query_params={"fields": "id,firstName:(localized),lastName"},
)
print("\n\nUsage with field projections:", response.entity)

