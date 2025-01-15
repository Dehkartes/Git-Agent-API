import requests

# GitHub API URL 및 인증
GITHUB_API_BASE = "https://api.github.com"

def get_pull_requests(github_token, repo_owner, repo_name, branch="main"):
	"""
	Fetches open pull requests for the given repository and branch.
	"""
	url = f"{GITHUB_API_BASE}/repos/{repo_owner}/{repo_name}/pulls"
	headers = {"Authorization": f"Bearer {github_token}"}
	params = {"state": "open", "base": branch}
	
	response = requests.get(github_token, url, headers=headers, params=params)
	if response.status_code == 200:
		return response.json()
	else:
		raise Exception(f"Failed to fetch pull requests: {response.status_code}, {response.text}")

def approve_pull_request(repo_owner, repo_name, pr_number, github_token):
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
