# -*- coding: utf-8 -*-

import sqlite3
import operator
import os

db_path = '/Users/utilisateur/Documents/workspace/Internship/text_mining/data/war/pubmed-result-war-abstarct-31547-1-pubmed-result-war-abstarct-db.db'
list_path = '/Users/utilisateur/Documents/workspace/Internship/text_mining/data/war/ListWar.txt'
list_files_path = '/Users/utilisateur/Documents/workspace/Internship/lists/'
files_of_list = []
con = sqlite3.connect(db_path)
cur = con.cursor()
cmd = cur.execute
cmdm = cur.executemany


def list_content(word):
    i = 1
    for file in os.listdir(list_files_path):
        if(file.endswith(".txt")):
            with open(list_files_path + file, 'r') as f:
                for data in f.readlines():
                    if (word in data.replace("\n","") and (len(word) == len(data.replace("\n","")))):
                        return i
            i += 1
    return 0

def get_file_list(filename=list_path):
    with open(filename, 'r') as f:
        for line in f:
            yield line.replace('\n', '')

def intersection(xs, ys):
    return [x for x in xs if x in ys]

def terms():
    cmd("select distinct data from ISIterms")
    return [x[0] for x in cur.fetchall()]

def get_cluster():
    cmd("select distinct id from cluster_files")
    return [x[0] for x in cur.fetchall()]

def query_word(word):
    cmd("select distinct id from ISIterms where data=? collate nocase", (word,))
    # fetchall() returns a list of tuples....
    return [x[0] for x in cur.fetchall()]

def cooccurrence(word1, word2):
    return intersection(query_word(word1), query_word(word2))

def get_title(article_id):
    cmd("select data from ArticleTitle where id=? limit 1", (article_id,))
    return cur.fetchone()[0]


def get_abstract(article_id):
    cmd("select data from Abstract where id=?", (article_id,))
    return [x[0] for x in cur.fetchall()]

def get_pmid(article_id):
    cmd("select data from PMID where id=? limit 1", (article_id,))
    return cur.fetchone()[0]

def get_articles(article_ids):
    return [(get_title(aid), get_pmid(aid), get_abstract(aid)) for aid in article_ids]

def get_co_articles(word1, word2):
    #return get_articles(get_all_cooccurrence(word1, word2))
    return get_articles(cooccurrence(word1, word2))


def set_cooccurrence_table():
    table_name = 'Cooccurrence'
    cmd('drop table if exists {}'.format(table_name))
    cmd('create table {}(term1 text, term2 text, cooccurrence integer)'.format(table_name))
    terms = sorted([term.lower() for term in get_file_list(list_path)])
    di = {}
    for term in terms:
        di[term] = query_word(term)
    for i in xrange(len(terms)):
        for j in xrange(i+1, len(terms)):
            t1 = terms[i]
            t2 = terms[j]
            co = len(intersection(di[t1], di[t2]))
            if co:
                cmd('insert into {} values(?, ?, ?)'.format(table_name), (t1, t2, co))
    cmd('create index if not exists co1_index on {}(term1, term2)'.format(table_name))
    cmd('create index if not exists co2_index on {}(term2)'.format(table_name))

def write_cooccurrence(filename):
    f = open(filename, 'w')
    terms = [ t for t in get_file_list(list_path)]
    di = {}
    for term in terms:
        di[term] = query_word(term)
    for i in xrange(len(terms)):
        for j in xrange(i+1, len(terms)):
            t1 = terms[i]
            t2 = terms[j]
            co = len(intersection(di[t1], di[t2]))
            if co:
                f.write('{},{},{}\n'.format(t1, t2, co))
    f.close()

def set_indices():
    cmd('create index if not exists term_index on ISIterms(data)')
    cmd('create index if not exists pmid_index on PMID(id)')
    cmd('create index if not exists title_index on Title(id)')
    cmd('create index if not exists abstract_index on Abstract(id)')

def get_cooccurrences(word):
    cmd('select distinct term2, cooccurrence from Cooccurrence where term1=? collate nocase', (word,))
    li1 = cur.fetchall()
    cmd('select distinct term1, cooccurrence from Cooccurrence where term2=? collate nocase', (word,))
    li2 = cur.fetchall()
    return sorted(li1 + li2, key=operator.itemgetter(1), reverse=True)

def get_one_cooccurrence(word1, word2):
    word1, word2 = word1.lower(), word2.lower()
    if word1 > word2:
        word1, word2 = word2, word1
    cmd('select cooccurrence from Cooccurrence where term1="{}" and term2="{}" '.format(word1, word2))
    res = cur.fetchone()
    if res:
        return res[0]
    else:
        return 0
        
        
def get_all_cooccurrence(word1, word2):
    word1, word2 = word1.lower(), word2.lower()
    if word1 > word2:
        word1, word2 = word2, word1
    cmd('select cooccurrence from Cooccurrence where term1="{}" and term2="{}" '.format(word1, word2))
    res = cur.fetchall()
    if res:
        return res
    else:
        return 0        
