Doc:

1   The import use file name as string parameter,
    if the file name has a '.' prefix,remove it.

2   If target file is not in the same dir of current file,
    search the file in subdir of current dir first then parrent,
    then grand parrent then parrent of grandparrent,etc.
    If found ,stop searching ,and use it.
