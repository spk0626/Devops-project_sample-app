from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptoContext
from jose import jwt, JWTError
from dotenv import load_dotenv
import os
from .database import SessionLocal

