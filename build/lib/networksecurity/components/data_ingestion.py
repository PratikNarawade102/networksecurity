from networksecurity.exception .exception import NetworkSecurityException
from networksecurity.logging_utils.logger import logging

## Configuration of the data ingestion
from networksecurity.entity.config_entity import DataIngestionCongif
import os
import sys
import numpy as np
import pymongo
from typing import List
from sklearn.model_selection import train_test_split

