#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import nltk
import langdetect

df = pd.read_csv("browsing_data.csv")

def remove_prefix(df):
    result = [ ]
    for item in df["header"].tolist():
        if "\xa0" in item:
            (_, new_item) = item.split("\xa0")
            result.append(new_item)
        else:
            result.append(item)
    data = df[["website", "link", "time"]]
    data["header"] = result
    data = data[["website", "link", "header", "time"]]
    return data

def count_words(df):
    word_map = { }
    for item in df["header"].tolist():
        words = item.split(' ')
        for word in words:
            if word in word_map:
                word_map[word] += 1
            else:
                word_map[word] = 1
    result = [ ]
    for key in word_map.keys():
        result.append((key, word_map[key]))
    result.sort(key = lambda x: x[1], reverse = True)
    return result

def extract_time(df):
    df = df.copy()
    month_table = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]
    years = [ ]
    months = [ ]
    days = []
    hours = []
    minutes = [ ]
    seconds = [ ]
    for date in df["time"]:
        segments = date.replace(',', '').split(' ')
        month, day, year, time, flag, _ = segments
        hour, minute, second = time.split(':')
        hour, minute, second = int(hour), int(minute), int(second)
        if flag == "PM":
            hour = hour + 12
        def month_to_int(month):
            for i in range(len(month_table)):
                if month in month_table[i]:
                    return (i + 1)
            return (-1)
        month = month_to_int(month)
        years.append(int(year))
        months.append(month)
        days.append(int(day))
        hours.append(hour)
        minutes.append(minute)
        seconds.append(second)
    df["year"] = years
    df["month"] = months
    df["day"] = days
    df["hour"] = hours
    df["minute"] = minutes
    df["second"] = seconds
    return df

def keep_only_english(df):
    keep = [ ]
    a2z = "abcdefghijklmnopqrstuvwxyz"
    letter_set = set(a2z + a2z.upper())
    def is_english(header):
        for c in header:
            if c in letter_set or c.isdigit() or c == ',' or c == '-' or c == '.' or c.isspace():
                pass
            else:
                return False
        return True
    for header in df["header"]:
#        try:
#            if langdetect.detect(header) == "en":
#                keep.append(True)
#            else:
#                keep.append(False)
#        except:
#            keep.append(False)
        keep.append(is_english(header))
    return df[keep]
            
def extract_words(df):
    text = " ".join([header for header in df["header"]])
    tokens = nltk.word_tokenize(text)
    return nltk.pos_tag(tokens)

df = remove_prefix(df)
word_map = count_words(df)
df = extract_time(df)
df.to_csv("browsing_records.csv", index = False)
df = keep_only_english(df)
df.to_csv("english_browsing_records.csv", index = False)
tokens = extract_words(df)
