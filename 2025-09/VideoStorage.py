'''
Video Storage
Given a video size, a unit for the video size, a hard drive capacity, and a unit for the hard drive, return the number of videos the hard drive can store using the following constraints:

The unit for the video size can be bytes ("B"), kilobytes ("KB"), megabytes ("MB"), or gigabytes ("GB").
If not given one of the video units above, return "Invalid video unit".
The unit of the hard drive capacity can be gigabytes ("GB") or terabytes ("TB").
If not given one of the hard drive units above, return "Invalid drive unit".
Return the number of whole videos the drive can fit.
Use the following conversions:
Unit	Equivalent
1 B	1 B
1 KB	1000 B
1 MB	1000 KB
1 GB	1000 MB
1 TB	1000 GB
For example, given 500, "MB", 100, and "GB as arguments, determine how many 500 MB videos can fit on a 100 GB hard drive.
'''

def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    if video_unit == "B" :
        # if drive_unit == "GB":
        #     total = (drive_size * 1000 * 1000 * 1000) / video_size
        #     video_size = int(total)
        # elif drive_unit == "TB":
        #     total = (drive_size * 1000 * 1000 * 1000 * 1000) / video_size
        #     video_size = int(total)
        # else:
        #     video_size = "Invalid drive unit"
        video_size = "Invalid video unit"
    elif video_unit == "KB":
        if drive_unit == "GB":
            total = (drive_size * 1000 * 1000) / video_size
            video_size = int(total)
        elif drive_unit == "TB":
            total = (drive_size * 1000 * 1000 * 1000) / video_size
            video_size = int(total)
        else:
            video_size = "Invalid drive unit"
    elif video_unit == "MB":
        if drive_unit == "GB":
            total = (drive_size * 1000 ) / video_size
            video_size = int(total)
        elif drive_unit == "TB":
            total = (drive_size * 1000 * 1000) / video_size
            video_size = int(total)
        else:
            video_size = "Invalid drive unit"
    elif video_unit == "GB":
        if drive_unit == "GB":
            total = (drive_size ) / video_size
            video_size = int(total)
        elif drive_unit == "TB":
            total = (drive_size * 1000) / video_size
            video_size = int(total)
        else:
            video_size = "Invalid drive unit"
    else:
        video_size = "Invalid video unit"

    return video_size

t = number_of_videos(500, "MB", 100, "GB")
print(t)
t1 = number_of_videos(2000, "MB", 100000, "MB")
print(t1)