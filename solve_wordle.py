answer_word = ["e", "", "", "", ""]  # 含む文字
answer_word2 = ["g", "", "e", "", "s"]  # 何番目か指定
answer_word3 = ["", "", "", "", ""]  # その番目ではない
exclusion_word = "proxywitchbradf"  # 除外する文字
exclusion_word_list = list(exclusion_word)

word_list = []
word_list2 = []
word_list3 = []
word_list4 = []


# googleの頻出単語10000から5文字の単語だけ抽出
with open('data/google-10000-english-no-swears.txt', mode='r') as f:
    google_word_list = f.read().split('\n')
    word_list = [word for word in google_word_list if len(word) == 5]

# その単語に指定した文字が入っているか
print("---------------in", answer_word, "------------------")
for word in word_list:
    if all(x in word for x in answer_word):
        word_list2.append(word)
print("---------------", len(word_list2), "------------------")

print("---------------at", answer_word2, "------------------")
# その単語が何文字目か
for word in word_list2:
    true_falselist = []
    for i in range(5):
        if answer_word2[i] == "" or word.find(answer_word2[i]) == i:
            true_falselist.append(True)
        else:
            true_falselist.append(False)
    if all(true_falselist):
        # if all(word.find(answer_word2[x])-1 == x for x in range(5)):
        word_list3.append(word)
print("---------------", len(word_list3), "------------------")
if len(word_list3) < 5:
    print(word_list3)

print("---------------not at", answer_word3, "------------------")
# その単語が何文字目ではないか
for word in word_list3:
    true_falselist = []
    for i in range(5):
        if answer_word3[i] == "" or word.find(answer_word3[i]) != i:
            true_falselist.append(True)
        else:
            true_falselist.append(False)
    if all(true_falselist):
        # if all(word.find(answer_word2[x])-1 == x for x in range(5)):
        word_list4.append(word)
print("---------------", len(word_list4), "------------------")


print("------------exclude", exclusion_word, "------------------")
# その単語に指定した文字が入ってないか
for word in word_list4:
    if all(x not in word for x in exclusion_word_list):
        print(word)
