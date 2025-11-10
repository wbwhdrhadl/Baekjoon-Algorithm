index_score = []

index_score = [("A+",4.5),("A0",4.0),("B+",3.5),("B0",3.0)
              ,("C+",2.5),("C0",2.0),("D+",1.5),("D0",1.0)
              ,("F",0.0)]
grade_dict = dict(index_score)

subject_list = []
total_sum = 0
result_sum = 0
while True:
    try:
        line = input().strip()
        if not line:
            break  # 빈 줄 입력 시 종료
        name, credit, score = line.split()  # 성적(A+, B0 등)은 무시
        if score!='P':
            subject_list.append((name, float(credit),score))
    except EOFError:
        break  # Ctrl+D 또는 Ctrl+Z로 입력 종료
avg_result = [credit for (_,credit,_) in subject_list]
subject_score = [score for (_,_,score) in subject_list]
for i in range(len(subject_list)):
    result_sum = result_sum + grade_dict[subject_score[i]]*avg_result[i]
    total_sum = total_sum + avg_result[i]
print(round(result_sum/total_sum,6))
    
