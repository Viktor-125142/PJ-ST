from fastapi import APIRouter
from transformers import FSMTForConditionalGeneration, FSMTTokenizer

from shemas.shemas import Item


transliteration = APIRouter()


name = "facebook/wmt19-ru-en"
tokenizer = FSMTTokenizer.from_pretrained(name)
model = FSMTForConditionalGeneration.from_pretrained(name)


@transliteration.get("/")
def root():
    return {"message": "hello world"}


@transliteration.post("/predict/")
async def interpreter(item: Item):
    input_ids = tokenizer.encode(item.text, return_tensors="pt")
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"result": decoded}
