'''
File Storage
Given a file size, a unit for the file size, and hard drive capacity in gigabytes (GB), return the number of files the hard drive can store using the following constraints:

The unit for the file size can be bytes ("B"), kilobytes ("KB"), or megabytes ("MB").
Return the number of whole files the drive can fit.
Use the following conversions:
Unit	Equivalent
1 B	1 B
1 KB	1000 B
1 MB	1000 KB
1 GB	1000 MB
For example, given 500, "KB", and 1 as arguments, determine how many 500 KB files can fit on a 1 GB hard drive.
'''

def number_of_files(file_size, file_unit, drive_size_gb):

    if file_unit == "B":
        total = (drive_size_gb * 1000 * 1000*1000) / file_size
        file_size = int(total)
    elif file_unit == "KB":
        total = (drive_size_gb * 1000*1000) / file_size
        file_size = int(total)
    elif file_unit == "MB":
        total = (drive_size_gb * 1000) / file_size
        file_size = int(total)

    return file_size

t = number_of_files(500, "KB", 1)
print(t)