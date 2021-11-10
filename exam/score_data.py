from exam.models import exam, ExamHeldSubject, score
from student.models import student
import random

print('score data is here')
exam_held_qs = ExamHeldSubject.objects.all()
# print(qs)

counter = 0
for exam_held_q in exam_held_qs:
    counter += 1
    max_marks = exam_held_q.exam.max_marks
    student_qs = student.objects.filter(Class=exam_held_q.subject.Class)
    # print(student_qs)
    # print(exam_held_q.exam.max_marks, exam_held_q.subject)
    for student_q in student_qs:
        # print(student_q.id)
        marks = random.randint(0, max_marks)
        score_o = score(exam_held=exam_held_q, stu=student_q, score=marks)
        score_o.save()
    
print(counter)    


