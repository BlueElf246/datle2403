import math
import numpy as np
while True:
    try:
        option=int(input('please choose your option:\n1:Ques1\n2:Ques2\n3:Ques3\n4:Ques4\n'))
        break
    except:
        print('nhap lai')
        continue
if option==1:
    lst1=[1,2,3]
    lst2=[1.0, 'Jessa', 3 ]
    lst3=[]
    print(lst1, lst2, lst3)
    print('this is Q1.2')
    list1=['M', 'na', 'i','Ke']
    list2=['y','me','s','lly']
    new_list=[]
    for x in range(len(list1)):
        new_string= str(list1[x]+list2[x])
        new_list.append(new_string)
    print(new_list)
if option==2:
    lst=np.array([1,2,3,4,5,6,7])
    print(f'this is Q2.1:\n Given:\n{lst}')
    print('Its square')
    print(lst**2)
    decide=input('run Q2.2?(y/n)\n')
    if decide=='y':
        print('this is Q2.2:\n')
        list1=['Hello','take']
        list2=['Dear', 'Sir']
        new_list=[]
        for x in list1:
            for y in list2:
                string=x+' '+y
                new_list.append(string)
        print(new_list)
if option==3:
    print('this is Q3.1')
    eng1=dict()
    eng2=dict()
    eng3=dict()
    eng1['Ten']=10
    eng1['Twenty']=20
    eng1['Thirty']=30
    eng2['Thirty'] = 30
    eng2['Fourty'] = 40
    eng2['Fifty'] = 50
    for x in eng1:
        eng3[x]=eng3.get(eng1[x],eng1[x])
    for y in eng2:
        eng3[y]= eng3.get(eng2[y],eng2[y])
    decide=input('run Q3.2(y/n)')
    if decide =='y':
        eng={
            'class':{
                'student':{
                    'name':'Mike',
                    'mark':{
                        'Physics':70,
                        'History':80
                    }
                }
            }
        }
        print(eng['class']['student']['mark']['History'])

    elif decide=='n':
        decide1=input('Run Q3.3(y/n)?')
        if decide1 =='y':
            employee=['Kelly','Emma']
            default={'designation':'developer','salary':8000}
            eng=dict()
            for x in employee:
                eng[x]=default
            print(eng)
if option ==4:
    print('this is Q4.1\n')
    tuple=('Orange',[10,20,30],[5,15,25])
    print(tuple[1][1])
    print('this is Q4.2\n')
    tuple=(10,20,30,40)
    a,b,c,d=tuple
    print(a)
    print(b)
    print(c)
    print(d)
    print('this is Q4.3\n')
    tuple1=(11,22)
    tuple2=(99,88)
    tem=tuple1
    tuple1=tuple2
    tuple2=tem
    print('this is tuple 1:',tuple1)
    print('this is tuple 2:',tuple2)











