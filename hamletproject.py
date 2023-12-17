from collections import Counter
from bs4 import BeautifulSoup

# 단어 빈도를 계산하는 함수
def word_counts(lines, top_n):
    words = [word for line in lines for word in line.split()]
    word_counts = Counter(words)
    return word_counts.most_common(top_n)

# 대사를 담을 리스트
hamlet_lines = []

# XML 또는 HTML 문서를 파싱
with open('C:\\Users\\GY_Kim\\Desktop\\hamlet\\ham.xml', 'r', encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

# Hamlet의 대사 추출
for speaker in soup.find_all("sp", attrs={"who": "#Hamlet_Ham"}):
    lines = [word.text.lower() for line in speaker.find_all("ab") for word in line.find_all("w")]
    hamlet_lines.extend(lines)

# 가장 많이 사용된 단어 상위 10개 출력
top_words = word_counts(hamlet_lines, 10) 

import matplotlib.pyplot as plt

# 대사 리스트에서 단어 빈도 계산
word_counts = Counter(hamlet_lines)

# 가장 빈도가 높은 단어 25개 추출
top_words = word_counts.most_common(25)

# 히스토그램 그리기
words, counts = zip(*top_words)
plt.figure(figsize=(10, 5))
plt.bar(words, counts, color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 25 Words in Hamlet\'s Lines')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()