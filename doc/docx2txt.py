import docx2txt
import re
 
text = docx2txt.process("hyundai_insu_default.docx")
text = re.sub('제 [0-9]+ [조항호장]', '', text)
text = re.sub('[0-9]+. ', '', text)
text = re.sub('\\n[가-힣]. ', '', text)
text = re.sub('[^가-힣0-9a-zA-Z\\s.]', '', text)
new_txt = open('result1.txt', 'w',encoding='utf-8-sig')
new_txt.write(text)
new_txt.close()