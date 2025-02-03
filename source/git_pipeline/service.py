from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse
import httpx
import os

# GitHub API URL 및 인증
GITHUB_API_BASE = "https://api.github.com"

# GitHub OAuth Configuration
github_client_id = "Ov23liLz8ad8ck4aVsvd"
github_client_secret = "271f740f6a19899ad9d4c90ce707aab387a49170"
redirect_uri = "http://localhost:8501/git/callback"
auth_url = f"https://github.com/login/oauth/authorize?client_id={github_client_id}&redirect_uri={redirect_uri}&scope=repo"
GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token"
GITHUB_API_URL = "https://api.github.com/user"

def approve_pull_request(github_token, repo_owner, repo_name, pr_number):
	"""
	Approves a pull request using the GitHub API.
	"""
	url = f"{GITHUB_API_BASE}/repos/{repo_owner}/{repo_name}/pulls/{pr_number}/reviews"
	headers = {"Authorization": f"Bearer {github_token}"}
	data = {"event": "APPROVE"}
	
	response = requests.post(url, headers=headers, json=data)
	if response.status_code == 200:
		print(f"Pull Request #{pr_number} approved successfully!")
	else:
		raise Exception(f"Failed to approve PR #{pr_number}: {response.status_code}, {response.text}")

def pr_agent(github_token, repo_owner, repo_name, branch="main"):
	"""
	Automated Pull Request approval agent based on LLM judgement.
	"""
	try:
		# Open Pull Requests 가져오기
		prs = get_pull_requests(github_token, repo_owner, repo_name, branch)
		if not prs:
			print("No open pull requests found.")
			return

		# 자동 승인 조건 설정 (예: LLM 리뷰 결과 기반)
		for pr in prs:
			pr_number = pr["number"]
			pr_title = pr["title"]
			print(f"Processing Pull Request #{pr_number}: {pr_title}")

			# LLM 리뷰 로직 추가 | 1. PR 내용 가져오기 2. 코드 리뷰 생성 3. 승인 여부 결정

	except Exception as e:
		print(f"Error: {e}")

# todo: 클라에서 던진 풀리퀘스트 읽기 -> 풀리퀘스트 리뷰하기