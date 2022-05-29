
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from graph_generator import generate_graph


load_dotenv(".env")

origins = ["http://localhost:3000"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate_graph")
async def create_upload_file(file: UploadFile = File(...)):

    generate_graph(file)
    with open("net-with-colors.png.dot", "r") as file:
        graph = file.read()
    cleaned_data = graph.replace("\n", "")
    return {"data": cleaned_data}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8088)
