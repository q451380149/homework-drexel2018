#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Function: Get timestamp of all tags in Linux kernel. Convert timestamp and version into scatter diagram.
Purpose: Educational only, please do not use for other purpose!
"""

__author__ = "Shen Jiacheng, group 17 of CS 212, Lanzhou University"
__copyright__ = "Copyright 2020, Study Project in Lanzhou University , China"
__license__ = "GPL V3"
__version__ = "0.1"
__maintainer__ = ["Jiacheng Shen"]
__email__ = ["Shenjch18@lzu.edu.cn"]
__status__ = "Experimental"


from subprocess import Popen, PIPE
import matplotlib.pyplot as plt


class ReleaseTime:
    base = 1113690036  # timestamp of the first version release: v2.6.12
    month_time = 60 * 60 * 24 * 30

    def __init__(self, filename):
        self.filename = filename

    def gettag(self):
        """
        return all tags in kernel.
        """
        cmd = ["git", "tag"]
        p = Popen(cmd, cwd=self.filename, stdout=PIPE)
        data, res = p.communicate()
        return data.decode("utf-8").split("\n")

    def gettime(self, tag):
        """
        return the time in month of a specific tag and the tag itself.
        :param tag:
        :return:
        """
        cmd = ['git', 'log', '--pretty=format:"%ct"', "-1", tag]
        p = Popen(cmd, cwd=self.filename, stdout=PIPE)
        data, res = p.communicate()
        if data == b'':
            return [], []
        time_stamp = []
        this_tag = []
        for seconds in data.decode("utf-8").split("\n"):
            month = round((int(seconds.strip('"')) - ReleaseTime.base) / ReleaseTime.month_time)
            if month not in time_stamp:
                time_stamp.append(month)
                this_tag.append(tag[0:4])
            else:
                pass
        return time_stamp, this_tag


RT = ReleaseTime("D:/git repository/linux-stable")
x = []
y = []
for tag in RT.gettag():
    print(tag)
    time_stamp, this_tag = RT.gettime(tag)
    x += time_stamp
    y += this_tag
plt.scatter(x, y)
plt.title("version release month from June 2005")
plt.xlabel("month")
plt.ylabel("version")
plt.show()
