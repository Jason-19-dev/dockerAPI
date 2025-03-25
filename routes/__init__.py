
from flask import Blueprint, jsonify,request, make_response
from utils.db import get_db

db = next(get_db())