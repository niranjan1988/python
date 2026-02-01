try:
    file_name="sample.txt"
    with open(file_name, "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("File read successfully.")
finally:
    print("Execution completed.")
    