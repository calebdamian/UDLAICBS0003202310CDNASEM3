# Testing file

from configparser import ConfigParser
import traceback
from extract.extract_channels import ext_channels
from extract.extract_countries import ext_countries
from extract.extract_customers import ext_customers
from extract.extract_products import ext_products
from extract.extract_promotions import ext_promotions
from extract.extract_sales import ext_sales
from extract.extract_times import ext_times
from transform.transformations import *
from util.get_db_conn import get_db_conn

try:
    print(get_db_conn("sor").start())
    # ext_channels()

except:

    traceback.print_exc()
finally:
    pass
