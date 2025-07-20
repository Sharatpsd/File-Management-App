from typing import Optional

def greet(name: Optional[str] = None) -> str:
    if name:
        return "Hello " + name
    else:
        return "Hello there!"

print(greet())          # Output: Hello there!
print(greet("Sharat"))  # Output: Hello Sharat
