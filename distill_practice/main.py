import pandas as pd
from datasets import load_dataset
import anthropic

ds = load_dataset("dreamerdeo/finqa")

client = anthropic.Anthropic(
)





def process_call(prompt):

    client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Hello, Claude"}
        ]
    )ture=0,
    )
    result = completion.model_dump()

    return result["choices"][0]["text"].strip()
