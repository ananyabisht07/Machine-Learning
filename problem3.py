import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('student.csv')
print(df)
Stu_marks=df['Marks']
Stu_name=df['Student_name']
plt.pie(Stu_marks,labels=Stu_name,autopct='%1.1f%%',shadow=True)
plt.title("Performance of students acccording to their marks")
plt.show()
