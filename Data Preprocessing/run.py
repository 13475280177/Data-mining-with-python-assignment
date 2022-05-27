import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA


def Question1():
    # read data file
    grade = pd.DataFrame(pd.read_csv('specs/Students_Results.csv',index_col=False))
    # replace Null with 0;
    grade = grade.fillna(0)
    # find min,max,mean and standard deviation for each column
    # min
    # homework1_min=grade['Homework 1'].min()
    # homework2_min = grade['Homework 2'].min()
    # homework3_min = grade['Homework 3'].min()
    # exam_min = grade['Exam'].min()
    # # max
    # exam_max = grade['Exam'].max()
    # homework3_max = grade['Homework 3'].max()
    # homework2_max = grade['Homework 2'].max()
    # homework1_max = grade['Homework 1'].max()
    # # mean
    # exam_mean = grade['Exam'].mean()
    # homework3_mean = grade['Homework 3'].mean()
    # homework2_mean = grade['Homework 2'].mean()
    # homework1_mean = grade['Homework 1'].mean()
    # # standard deviation
    # exam_std = grade['Exam'].std()
    # homework3_std = grade['Homework 3'].std()
    # homework2_std = grade['Homework 2'].std()
    # homework1_std = grade['Homework 1'].std()
    # print('homework1_min: '+str(homework1_min)+' homework2_min: '+str(homework2_min)+' homework3_min: '+str(homework3_min)+' Exam_min: '+str(exam_min)+'\n')
    # print('homework1_max: '+str(homework1_max)+' homework2_max: '+str(homework2_max)+' homework3_max: '+str(homework3_max)+' Exam_max: '+str(exam_max)+'\n')
    # print('homework1_mean: '+str(homework1_mean)+' homework2_mean: '+str(homework2_mean)+' homework3_mean: '+str(homework3_mean)+' Exam_mean: '+str(exam_mean)+'\n')
    # print('homework1_std: '+str(homework1_std)+' homework2_std: '+str(homework2_std)+' homework3_std: '+str(homework3_std)+' Exam_std: '+str(exam_std)+'\n')

    #Add an additional named as ‘Homework Avg’ for the average homework mark for each student.Keep one decimal place
    grade['Homework Avg'] = grade[['Homework 1','Homework 2','Homework 3']].mean(1).round(1)
    # add an additional column named 'Overall Mark' for the overall folded mark.
    grade['Overall Mark'] = grade['Homework Avg']*0.25+grade['Exam']*0.75
    # correlation matrix
    # co=grade.corr()
    # grade
    grade['Grade'] = grade['Overall Mark'].apply(lambda x: get_letter_grade(x))
    # draw histogram

    # grade['Grade'].hist()
    # plt.show()



    grade.to_csv('./output/question1_out.csv', index=False)

def Question2():
    data = pd.DataFrame(pd.read_csv('./specs/Sensor_Data.csv',index_col=False))
    # copy the attribute 3 and 12
    data['Original Input3'] = data['Input3']
    data['Original Input12'] = data['Input12']
    # z-score transformation,z = (x – μ) / σ
    data['Input3'] = (data['Original Input3']-data['Original Input3'].mean())/data['Original Input3'].std()
    # 0-1 transformation (z-min)/(max-min)
    data['Input12'] = (data['Original Input12']-data['Original Input12'].min())/(data['Original Input12'].max()-data['Original Input12'].min())
    # calculate the average of all the attributes from “Input1” to “Input12” as new attributes
    data['Average Input'] = data[['Input1','Input2','Input3','Input4','Input5','Input6','Input7','Input8','Input9','Input10','Input11','Input12']].mean(1)





    data.to_csv('./output/question2_out.csv', index=False)

def Question3():
    dna_Data=pd.DataFrame(pd.read_csv('./specs/DNA_Data.csv'))
    pca = PCA()
    pca.fit(dna_Data)

    # The spacing of each bin is the same
    a = pd.cut(pca.explained_variance_, 10)
    # The frequencies of the numbers contained are the same
    b = pd.qcut(pca.explained_variance_, 10)

    for i in range(22):
        dna_Data['pca' + str(i) + '_width']=a[i]
    for i in range(22):
        dna_Data['pca' + str(i) + '_freq']=b[i]
    dna_Data.to_csv('./output/question3_out.csv', index=False)





def get_letter_grade(mark):
    if mark>=90:
        return "A+"
    elif mark>=80:
        return "A"
    elif mark>=70:
        return "A-"
    elif mark>=66.67:
        return "B+"
    elif mark>=63.33:
        return "B"
    elif mark>=60:
        return "B-"
    elif mark>=56.67:
        return "C+"
    elif mark>=53.33:
        return "C"
    elif mark>=50:
        return "C-"
    elif mark>=46.67:
        return "D+"
    elif mark>=43.33:
        return "D"
    elif mark>=40:
        return "D-"
    elif mark >= 36.67:
        return "E+"
    elif mark >= 33.33:
        return "E"
    elif mark >= 30:
        return "E-"
    elif mark>=26.67:
        return "F+"
    elif mark>=23.33:
        return "F"
    elif mark>=20:
        return "F-"
    elif mark>=16.67:
        return "G+"
    elif mark>=13.33:
        return "G"
    elif mark>=0.01:
        return "G-"
    elif mark == 0:
        return "NM"
    else:
        return "ABS"



if __name__=="__main__":
    question1 = Question1()
    question2 = Question2()
    question3 = Question3()

