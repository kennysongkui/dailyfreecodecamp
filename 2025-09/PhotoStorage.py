'''
Photo Storage
Given a photo size in megabytes (MB), and hard drive capacity in gigabytes (GB), return the number of photos the hard drive can store using the following constraints:

1 gigabyte equals 1000 megabytes.
Return the number of whole photos the drive can store.
'''

def number_of_photos(photo_size_mb, drive_size_gb):
    total = (drive_size_gb * 1000)/photo_size_mb
    photo_size_mb = int(total)
    return photo_size_mb

t = number_of_photos(3.5, 750)
print(t)