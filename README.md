# Word Calculator

A Python calculator that evaluates arithmetic expressions written in plain English words.

```python
calc("twenty five plus thirteen")   # → "thirty eight"
calc("six multiply by seven")       # → "forty two"
calc("ten divide by zero")          # → "error: division by zero"
```

---

## Features

- **Four operations** — `plus`, `minus`, `multiply`, `divide`
- **Compound numbers** — supports two-word numbers like `twenty five`, `ninety nine`
- **Optional `by`** — `multiply by` and `divide by` both work, `by` is optional
- **Word output** — result is returned as English words, not digits
- **Graceful errors** — descriptive error strings for division by zero, unknown words, missing operands, empty input
- **No dependencies** — stdlib only (`operator`, `re`)

---

## Requirements

Python 3.6+

---

## Usage

```bash
git clone https://github.com/Shipovmax/calculator
cd calculator
python main.py
```

Or import directly:

```python
from main import calc

print(calc("nine divide by three"))   # three
print(calc("forty plus fifty"))       # ninety
print(calc("five minus eight"))       # minus three
```

---

## Supported Range

Numbers 0–99 (zero through ninety nine). Results outside this range are returned as words where possible; floats are rounded to 2 decimal places.

---

## Error Handling

| Input | Output |
|-------|--------|
| `"five plus"` | `"error: missing right operand"` |
| `"ten divide by zero"` | `"error: division by zero"` |
| `"five plus unknown"` | `"error: unknown word 'unknown'"` |
| `""` | `"error: empty expression"` |
| `"five"` | `"error: operator not found (use plus, minus, multiply, divide)"` |

---

## Author

- GitHub: [Shipovmax](https://github.com/Shipovmax)
- Email: shipov.max@icloud.com
