import base64
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

def generate(code):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=code),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are a professional software engineer and AI assistant.

Your task is to analyze Python functions and generate:
1. A clear, plain-English summary of what each function does
2. A Python-style docstring for the function
3. An estimate of the function's time and space complexity using Big-O notation

Return your output in the following structured format for each function:

---
Function: <function_name>(<parameters>)
→ <summary>
Docstring:
\"\"\"
<docstring>
\"\"\"
Time Complexity: O(?)
Space Complexity: O(?)
---

### Examples

Here is an example function:
```python
def add(a, b):
    return a + b

Expected Output
Function: add(a,b) => Returns the sum of the input values
Doctstring: \"\"\" Adds two numbers and returns the result \"\"\"
Args: a (int or float): First number , b (int or float): Second number.
Returns: int or float: Sum of a and b
Time Complexity: O(1)
Space Complexity: O(1)
"""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    code =""" def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)"""

    generate(code)
