import boto3
from camelcase import CamelCase
c = CamelCase()
txt = "hello world"
print(c.hump(txt))
