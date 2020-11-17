# -*- coding: utf-8 -*
from time import sleep
import json
import random
import sys
import os
from model.api_log_test import APILogModel


sql_json_arr={}
sql_json_arr['contents']='1'
crw_log_data = APILogModel(**sql_json_arr)
crw_log_data.save_to_db()