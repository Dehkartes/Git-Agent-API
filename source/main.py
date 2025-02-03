from fastapi import FastAPI, Request, status
from fastapi.responses import Response
from source.allow_ip import ALLOWED_IPS
import uvicorn

from git_pipeline.router import router as gitRouter

app = FastAPI()

app.include_router(gitRouter)

@app.middleware("http")
async def ip_filter_middleware(request: Request, call_next):
	client_ip = request.client.host
	if client_ip not in ALLOWED_IPS:
		return Response(status_code=status.HTTP_403_FORBIDDEN)
	response = await call_next(request)
	return response

if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8000)