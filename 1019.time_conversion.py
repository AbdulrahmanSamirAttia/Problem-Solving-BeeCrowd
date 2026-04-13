"""
Read an integer value,
which is the duration in seconds of a certain event in a factory,
and inform it expressed in hours:minutes:seconds.

Input
The input file contains an integer N.

Output
Print the read time in the input file (seconds)
converted in hours:minutes:seconds like the following example.
"""

""" Solution (A) """
# duration = int(input().strip())
#
# hours = duration // 3600
# minutes = (duration % 3600) // 60
# seconds = duration % 60
#
# print(f"{hours:01}:{minutes:01}:{seconds:01}")

""" Solution (B) """
duration = int(input().strip())

print(f"{(duration // 3600):01}:{((duration % 3600) // 60):01}:{(duration % 60):01}")