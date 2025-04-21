# LLM-Powered Python Code Function Explainer

This project uses Google's Gemini API to analyze Python functions and generate structured outputs including:

- A plain-English summary
- A Python-style docstring
- Estimated time and space complexity in Big-O notation

This tool is helpful for code review, learning, auto-documentation, or AI model evaluation tasks.

## Example Output

**Input:**
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

**Output:**
```
---
Function: factorial(n)
→ Calculates the factorial of a number recursively.
Docstring:
"""
Calculates the factorial of a non-negative integer using recursion.

Args:
    n (int): A non-negative integer.

Returns:
    int: The factorial of the input number.
"""
Time Complexity: O(n)
Space Complexity: O(n)
---
```

## Setup Instructions

1. Clone the repository
```
git clone https://github.com/yourusername/code-analyzer.git
cd code-analyzer
```

2. Create a virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Configure your environment
Create a `.env` file with the following line:
```
GEMINI_API_KEY=your-google-gemini-api-key
```

## Usage

Open `main.py` and replace the value of the `code` variable with your Python function(s):
```python
code = """
def is_even(n):
    return n % 2 == 0
"""
```

Then run the script:
```
python explain.py
```

## License

This project is licensed under the MIT License.

