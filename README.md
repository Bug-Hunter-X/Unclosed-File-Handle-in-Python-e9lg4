# Unclosed File Handle in Python

This repository demonstrates a common error in Python where a file is opened but not properly closed, especially when exceptions are involved. This is a crucial area to pay attention to as it can lead to resource leaks and unexpected behavior in programs that handle files extensively.

## The Bug

The primary issue resides in the `function_with_unclosed_file` function.  If an exception occurs within the function's body, the `f.close()` statement may never be executed, leaving the file handle open.

## The Solution

The problem is resolved by using a `try...finally` block, which ensures that `f.close()` is always called, regardless of whether an exception occurs.

Alternatively, using the `with` statement provides a cleaner and more concise way to handle files, automating the closing process.