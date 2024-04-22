from fastapi import FastAPI

api = FastAPI(
    title="Shortened Url API"
)


@api.get("/{token}")
async def get_url_from_token(token: str):
    pass
    

