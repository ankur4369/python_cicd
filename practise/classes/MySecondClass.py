class New:
    def __init__(self):
        print("Initialising the new class")

    def __enter__(self):
        print(f"Starting the new object {self}")
    
    def __exit__(self, type, value, traceback):
        print(type, value, traceback)
        print(f"Ending the new object {self}")

# f = New()
print("Breaking")
with New() as g:
    print("Hello World")