import os

def find_files(suffix, path):

    if suffix == None or path == None or not os.path.exists(path):
        return []

    files_with_suffix = []

    for file_or_folder in os.listdir(path):

        file_or_folder_path = os.path.join(path, file_or_folder)

        if os.path.isfile(file_or_folder_path):
            file = file_or_folder_path

            if f"{file}".endswith(suffix):
                files_with_suffix.append(file)

        if os.path.isdir(file_or_folder_path):
            folder = file_or_folder_path
            files_with_suffix_in_folder = find_files(suffix, folder)
            files_with_suffix.extend(files_with_suffix_in_folder)

    return files_with_suffix




## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1: Basic Functionality
files_with_c_suffix = find_files(".c", "./testdir")
assert files_with_c_suffix == ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']

## Test Case 2: Empty Directory
files_with_c_suffix = find_files(".c", "./empty")
assert files_with_c_suffix == []

## Test Case 3: Null or Non-Existent Directory or Suffix
files_with_c_suffix = find_files(".c", "./i_dont_exist")
assert files_with_c_suffix == []

files_with_c_suffix = find_files(".c", None)
assert files_with_c_suffix == []

files_with_c_suffix = find_files(None, "./testdir")
assert files_with_c_suffix == []