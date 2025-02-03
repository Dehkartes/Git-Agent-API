from fastapi import APIRouter

from git_pipeline import service

router = APIRouter(prefix="/git")