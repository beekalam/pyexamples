# -*- coding: utf-8 -*-
import csv
import jalali as jalali
farsi_num = list(u'۰۱۲۳۴۵۶۷۸۹')
# print farsi_num

def stripfarsichars(item):
    ret = u''
    for     i in item:
        if i  in farsi_num:
            ret += unicode(i)
    return convert_farsinum_toascii(ret)

def convert_farsinum_toascii(item):
    ret = ''
    for v in item:
        ret += str(farsi_num.index(v))
    return ret

def make_iso_persian(persianstr):
    return persianstr[:4] + "-" + persianstr[4:6] + "-" + persianstr[6:]
    # return persianstr[:4]  + "-" + persianstr[6:] + "-" + persianstr[4:6]


def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]

filename='abc.csv'
file1reader = unicode_csv_reader(open(filename))
# print file1reader
# file1reader = file1reader[1:]
counter = 0
ret = []
for (radif, mande,bedh, bast, sharh, shomare_variz, name_variz, serial, code, shobe , zaman, tarikh) in file1reader:

    if counter != 0:
        namev = stripfarsichars(name_variz)
        tarikh_ = str(make_iso_persian(tarikh))
        if namev != '':
            tar =  jalali.Persian(tarikh_).gregorian_string()
            print "{0},{1}".format(namev, tar)
            ret.append([namev, tar])
    counter += 1
        # print jalali.Persian(tarikh_).gregorian_string()
    # print make_iso_persian(tarikh)


banklist = []
for (id, dat) in ret:
    (year, month, day) = dat.split('-')
    for bitem in banklist:
        (byear, bmonth, bday, time) = bitem.split('-')
        if byear == year and month == bmonth and day == bday:
            print
# for item in banklis
