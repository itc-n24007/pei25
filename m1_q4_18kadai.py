phrase = 'PythonProgramming'
list_p = []
for p in phrase:
    if p not in list_p :
        list_p.append(p)
print(len(phrase) - len(list_p))
re = "".join(list_p) # join()を使ってリスト内の文字列を一つにまとめる
print(re)
