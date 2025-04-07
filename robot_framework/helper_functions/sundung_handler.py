"""
docstring: This module contains functions to handle Sundung API requests and responses.
"""


import os
import sys
import json
import urllib.parse

from io import BytesIO

from datetime import datetime, timedelta

from sqlalchemy import create_engine

import openpyxl

import pandas as pd

from OpenOrchestrator.orchestrator_connection.connection import OrchestratorConnection
from itk_dev_shared_components.smtp import smtp_util

from mbu_dev_shared_components.os2forms import forms

from mbu_dev_shared_components.msoffice365.sharepoint_api.files import Sharepoint

from robot_framework.helper_functions.sundung_handler import SundungHandler


def main():




    return