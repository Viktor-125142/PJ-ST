import uvicorn


if __name__ == "__main__":
    uvicorn.run("fast_viktor:app", host="localhost", port=8000)
