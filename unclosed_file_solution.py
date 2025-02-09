def function_with_unclosed_file_solution(filename):
    try:
        f = open(filename, 'w')
        # ... some code that might raise an exception ...
        f.write('Hello, this is a test!')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        f.close()
        print("File closed.")

#A better way to handle file operations is using the "with" statement:
def function_with_with_statement(filename):
    try:
        with open(filename, 'w') as f:
            f.write('This is written using with statement')
    except Exception as e:
        print(f"An error occurred: {e}")
    print("File automatically closed by 'with' statement.")     