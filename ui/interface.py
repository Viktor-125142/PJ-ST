import gradio as gr
from transformers import FSMTForConditionalGeneration, FSMTTokenizer

from shemas.shemas import Item


name = "facebook/wmt19-ru-en"
tokenizer = FSMTTokenizer.from_pretrained(name)
model = FSMTForConditionalGeneration.from_pretrained(name)

title = "Переводчик"


def interpreter(text: str):
    item = Item(text=text)
    input_ids = tokenizer.encode(item.text, return_tensors="pt")
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded


examples = [
    ["Как дела?"],
    ["Я хочу кушать"],
    ["Дай в займы до пятнице"],
]


demo = gr.Interface(
    fn=interpreter,
    inputs=gr.Text(label="Введите текст на русском"),
    outputs=gr.Text(label="Перевод на английском"),
    title=title,
    examples=examples,
)

if __name__ == "__main__":
    demo.launch()

