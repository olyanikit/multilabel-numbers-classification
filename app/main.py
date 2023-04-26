from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import numpy as np
import json
from PIL import Image 
import torch
from torchvision.io import read_image
from torchvision import transforms as T
from onnxruntime import InferenceSession


app = FastAPI()

onnx_model = '/code/./app/model/numbers.onnx'


@app.post("/upload")
async def create_file(request: Request):
    form = await request.form()
    img = Image.open(form['file'].file)
    img = img.convert('RGB')
    img.save("test.jpg")
    img = read_image('test.jpg')
    img = T.transforms.Grayscale()(img)
    img = T.transforms.Resize((28, 56))(img)
    img = img.clone().detach()
    img = torch.unsqueeze(img, 0)/255
    data = json.dumps({'data': img.tolist()})
    data = np.array(json.loads(data)['data']).astype('float32')
    session = InferenceSession(onnx_model, None)
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name
    result = session.run([output_name], {input_name: data})
    max_indices = np.argsort(np.array(result).squeeze())[-2:][::-1]
    prediction = "".join(map(lambda x: str(x), max_indices.tolist()))
    return prediction

@app.get("/")
def main():
    def iter_file():
        with open("/code/./app/temp/item.html", 'rb') as f:
            yield from f
    return StreamingResponse(iter_file(), media_type="text/html")