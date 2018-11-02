#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import nltk
import langdetect
from nltk.corpus import stopwords
import networkx as nx
import matplotlib.pyplot as plt

pd.options.display.max_columns = 9999

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
    stopwords_set = set(stopwords.words('english'))
    words = [ ]
    for token in tokens:
        if not (token in stopwords_set):
            words.append(token)
    tagged_words = nltk.pos_tag(words)
    result = [ ]
    for word in tagged_words:
        (text, pos) = word
        if len(pos) >= 2 and pos[0:2] == "NN":
            result.append(text)
    return result

def count_occurrence(df, words):
    word_list = list(set(words))
    word_map = { }
    for word in word_list:
        word_map[word] = 0
    for header in df["header"]:
        for word in word_list:
            if word in header:
                word_map[word] += 1
    result = [ ]
    for key in word_map.keys():
        result.append((key, word_map[key]))
    result.sort(key = lambda x: x[1], reverse = True)
    return result

def co_occurrence(df, interval, words):
    words = list(set(
            list(filter(lambda word: len(word) > 1, words))))
    df = df.copy()
    df["time_tag"] = df["year"] * 10000 * 10000 + df["month"] * 10000 * 100 + df["day"] * 10000 + df["hour"] * 100 + df["minute"]
    df = df.sort_values(by = "time_tag")
    headers = df["header"].tolist()
    times = df["time_tag"].tolist()
    connections = { }
    for i in range(len(df)):
        titles = [headers[i]]
        k = i + 1
        while k < len(df):
            if times[k] - times[i] < interval:
                titles.append(headers[k])
                k += 1
            else:
                break
        text = " ".join(titles)
        # TO DO: I will optimize this part in the future (- ^ -)
        
        selected_words = list(filter(lambda word: word in text, words))
        if len(selected_words) >= 2:
            for m in range(len(selected_words) - 1):
                for n in range(m + 1, len(selected_words)):
                    w1 = selected_words[m]
                    w2 = selected_words[n]
                    if (w1, w2) in connections:
                        connections[(w1, w2)] += 1
                    elif (w2, w1) in connections:
                        connections[(w2, w1)] += 1
                    else:
                        connections[(w1, w2)] = 1
    result = [ ]
    for key in connections.keys():
        result.append((key, connections[key]))
    result.sort(key = lambda x: x[1], reverse = True)
    return result

def make_connection_frame(connections):
    result = [ ]
    for connection in connections:
        words, count = connection
        word1, word2 = words
        result.append((word1, word2, count))
    return pd.DataFrame(result, columns = ["word1", "word2", "count"])

def make_word_graph(word_network):
    word1 = word_network["word1"].tolist()
    word2 = word_network["word2"].tolist()
    G = nx.Graph()
    for i in range(len(word1)):
        G.add_edge(word1[i], word2[i])
    return G
    
    
df = remove_prefix(df)
word_map = count_words(df)
df = extract_time(df)
df.to_csv("browsing_records.csv", index = False)
df = keep_only_english(df)
df.to_csv("english_browsing_records.csv", index = False)
tokens = extract_words(df)
word_map = count_occurrence(df, tokens)
connections = co_occurrence(df, 200, tokens)
word_connections = make_connection_frame(connections)
word_connections.to_csv("word_connections.csv", index = False)
word_network = word_connections[word_connections["count"] >= 5]
word_network.to_csv("word_network.csv", index = False)
G = make_word_graph(word_network)
