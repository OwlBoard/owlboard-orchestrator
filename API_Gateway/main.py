import os
import httpx
from fastapi import FastAPI, Request, Response
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

USER_SERVICE_URL = os.getenv("USER_SERVICE_URL")
COMMENTS_SERVICE_URL = os.getenv("COMMENTS_SERVICE_URL")

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def route_request(request: Request, path: str):
    async with httpx.AsyncClient() as client:
        target_url = ""
        if path.startswith("users"):
            target_url = f"{USER_SERVICE_URL}/{path}"
        elif path.startswith("dashboards") or path.startswith("comments"):
            target_url = f"{COMMENTS_SERVICE_URL}/{path}"
        else:
            return Response(content="Not Found", status_code=404)

        data = await request.body()
        headers = dict(request.headers)
        headers.pop("host", None)

        response = await client.request(
            method=request.method,
            url=target_url,
            content=data,
            headers=headers,
            params=request.query_params
        )

        return Response(
            content=response.content,
            status_code=response.status_code,
            headers=dict(response.headers)
        )