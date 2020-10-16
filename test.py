import pytumblr
import pprint

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  'eMQblB3BolxLugQYmxcQMTzfUCF4tvGBEcJPqFju9bLXd0GGOx',
  'Y09vRDZWL10IT48nZEnWhvPhLKydGIWIFgqEf7S3tREc3bHl2Z',
  '3ZWrqvetBpsRydRurZRlwbR4QxB9Z1yakXQbZrF3E860I6oyoh',
  'GIPSuUzHf3qeFpQUXs6m1Qu4cELdKyhcml3a9qhwN887LeBUjL'
)

# Make the request
pprint.pprint(client.dashboard())