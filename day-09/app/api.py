from fastapi import FastAPI
from routers import system_health_endpoint, logs, aws

tags_metadata = [
    {"name":"System_Health", "description":"Core health checks and root endpoints."},
    {"name":"Logs_Analysis", "description":"Log File analysis endpoints."},
    {"name":"Aws_resource", "description":"Aws resource endpoints."},
]

app=FastAPI(
    title="DevOps Tool API",
    description="A modular API for DevOps automation",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_tags=tags_metadata
)

#decorator
@app.get("/")
def hello():
    """
    Docstring for hello
    """
    return {"message":"DevOps utilites API"}

app.include_router(system_health_endpoint.router, tags=["System_Health"])
app.include_router(logs.router, tags=["Logs_Analysis"])
app.include_router(aws.router, tags=["Aws_resource"])