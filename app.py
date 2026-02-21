import pandas as pd

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 1:
            return False
    return True
    
def handler(event, context):
    print("hello lambda from zappa")
    es_primo(5)
    return{}