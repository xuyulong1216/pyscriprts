import random
import time

def pshow (to_display):
    to_display_0=[]
    to_display_str=''
    for k in to_display :
        for l in k :
            to_display_0.append(l)
        to_display_0.append('\n')
    to_display_str=to_display_str.join(to_display_0)
    return to_display_str

def generate(row,start_line,text):
    for n in range(len(text)):
        display[row][start_line+n]=text[n]

def data(row,start_line,text):
    for n in range(len(text)):
        data0[row][start_line+n]=text[n]

def map_generate():
    generate(0,0,'Reversi')
    generate(1,4,'A B C D E F G H')
    for m in range (2,10):
        generate(m,2,str(m-1))
        for o in range (2,10):
            generate(m,o+o,'.')
            data(m,o,'.')
            generate(m,o+o+1,' ')
            generate(3+2,5*2,'x')
            generate(4+2,6*2,'x')
            generate(3+2,6*2,'o')
            generate(4+2,5*2,'o')
            data(3+2,3+2,'x')
            data(4+2,4+2,'x')
            data(3+2,4+2,'o')
            data(4+2,3+2,'o')

def generate_place_list(x1,y1):
    tdr=[]
    for p in range (-1,2):
        for q in range (-1,2):
            if (data0[x1+p+1][y1+q+1]=='o'):
                tdr.append(1)
            else:
                tdr.append(0)
    return tdr

def m_generate_place_list(x_1,y_1):
    tdr1=[]
    for p in range (-1,2):
        for q in range (-1,2):
            if (data0[x_1+p+1][y_1+q+1]=='x'):
                tdr1.append(1)
            else:
                tdr1.append(0)
    return tdr1

def check_place(x2,y2,list1):
    s=0
    list_q=[]
    chck=1
    for r in list1:
        if (r != 0):
            t=1
            while True:
                t=t+1
                if (data0[x2+1+t*rev[s][0]][y2+1+t*rev[s][-1]]=='x'):
                    chck=0
                    break
                elif (data0[x2+1+t*rev[s][0]][y2+1+t*rev[s][-1]]=='.' or data0[x2+1+t*rev[s][0]][y2+1+t*rev[s][-1]]==' '):
                    list1[s]=0
                    break
                else:
                    continue
        s=s+1
    list_q.append(chck)
    list_q.append(list1)    
    return list_q

def m_check_place(x_2,y_2,list_1):
    s=0
    list_p=[]
    chck=1
    for r in list_1:
        if (r != 0):
            t=1
            while True:
                t=t+1
                if (data0[x_2+1+t*rev[s][0]][y_2+1+t*rev[s][-1]]=='o'):
                    chck=0
                    break
                elif (data0[x_2+1+t*rev[s][0]][y_2+1+t*rev[s][-1]]=='.' or data0[x_2+1+t*rev[s][0]][y_2+1+t*rev[s][-1]]==' '):
                    list_1[s]=0
                    break
                else:
                    continue
        s=s+1    
    list_p.append(chck)
    list_p.append(list_1)
    return list_p

def reverse(x3,y3,list2):
    w=0
    for v in list2:
        if (v != 0):
            z=0
            while True :
                z=z+1
                
                if (data0[x3+1+z*rev[w][0]][y3+1+z*rev[w][-1]]=='o'):
                    generate(x3+1+z*rev[w][0],y3*2+2*z*rev[w][-1]+2,'x')
                    data(x3+1+z*rev[w][0],y3+1+z*rev[w][-1],'x')
                else:
                    break
        w=w+1    
    
def m_reverse(x_3,y_3,list_2):
    w=0
    b=0
    for v in list_2:
        if (v != 0) :
            z=0
            while True :
                z=z+1
                
                if (data0[x_3+1+z*rev[w][0]][y_3+1+z*rev[w][-1]]=='x'):
                    generate(x_3+1+z*rev[w][0],y_3*2+2*z*rev[w][-1]+2,'o')
                    data(x_3+1+z*rev[w][0],y_3+1+z*rev[w][-1],'o')
                    b=b+1
                else:
                    break
        w=w+1    
    return b
        
display=[]
data0=[]
for i in range(11):
    display_x=[]
    data0_x=[]
    for j in range(20):
        display_x.append(' ')
        data0_x.append(' ')
    display.append(display_x)
    data0.append(data0_x)        
del display[-1]

map_generate()
to_str=pshow(display)
print(to_str)
rev=((-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1))
#show(data)
while True:
    place=input('Black (x): ')
    if (len(place) != 2):
        continue
    X=place[-1] #horizontal
    if ( X.isdigit() == False):
        continue
    y_s=place[0]
    x=int(X)
    Y=y_s.capitalize() #vertical
    y=ord(Y)-64
    if ( x>8 or y>8 or data0[x+1][y+1] != '.'):
        continue
    to_reverse_direction=generate_place_list(x,y)
    check=check_place(x,y,to_reverse_direction)[0]   
    if (check==1):
        continue
    ae=check_place(x,y,to_reverse_direction)
    to_reverse_direction_1=ae[-1]
    #print(to_reverse_direction_1)
    reverse(x,y,to_reverse_direction_1)
    
    generate(x+1,y*2+2,'x')
    data(x+1,y+1,'x')
    to_str=pshow(display)
    print(to_str)
    #data_str=pshow(data0)
    #print(data_str)
    e=0
    possible_place=[]
    for c in data0 :
        if (c == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] ):
            continue
        e=e+1
        f=0
        for d in c :
            if (d==' '):
                continue
            f=f+1           
            if (d != '.'):
                continue 
            else:
                m_to_reverse_direction=m_generate_place_list(e,f)
                #print(m_to_reverse_direction)
                if (m_to_reverse_direction == [0, 0, 0, 0, 0, 0, 0, 0, 0]):
                    continue
                else:
                    m_check=m_check_place(e,f,m_to_reverse_direction)[0]
                    if (m_check==0):
                        place=[e,f]
                        possible_place.append(place)
                    else:
                        continue
    if (possible_place==[]):
        print ('You Win')
        break

    sum_0=0
    for g in possible_place :
         sum_0=(g[0]-4.5)**2+(g[-1]-4.5)**2+sum_0
    avg=sum_0/len(possible_place)
    normalize_list=[]
    normalized=0
    for h in possible_place :
        normalized=((h[0]-4.5)**2+(h[-1]-4.5)**2)/avg+normalized
        normalize_list.append(normalized)
    rnd_num=random.uniform(0,len(possible_place))
    ac=0
    for aa in normalize_list :
        ab=rnd_num-aa
        ac=ac+1
        if (ab > 0):
            continue
        else:
            final_place=possible_place[ac-1]
            break
    m_reverse_list=m_generate_place_list(final_place[0],final_place[-1])
    ad=m_check_place(final_place[0],final_place[-1],m_reverse_list)
    m_reverse_list_1=ad[-1]
    print ('White (o):',chr(final_place[-1]+64),final_place[0])
    generate(final_place[0]+1,final_place[-1]*2+2,'o')
    data(final_place[0]+1,final_place[-1]+1,'o')
    m_reverse(final_place[0],final_place[-1],m_reverse_list_1)  
    to_str=pshow(display)
    print(to_str)
    ah=0
    h_possible_place=[]
    for ai in data0 :
        if (ai == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] ):
            continue
        ah=ah+1
        ak=0
        for aj in ai :
            if (aj==' '):
                continue
            ak=ak+1           
            if (aj != '.'):
                continue 
            else:
                to_reverse_direction=generate_place_list(ah,ak)
                #print(m_to_reverse_direction)
                if (to_reverse_direction == [0, 0, 0, 0, 0, 0, 0, 0, 0]):
                    continue
                else:
                    check1=check_place(ah,ak,to_reverse_direction)[0]
                    if (check1==0):
                        h_place=[ah,ak]
                        h_possible_place.append(h_place)
                    else:
                        continue
    if (h_possible_place==[]):
        print ('You Lose')
        break
    chessset=pshow(data0)
    if ('x' not in chessset and '.' in chessset):
        print ('You Lose')
        break
    elif('.' not in chessset):
        black_count=0
        white_count=0
        for af in data0:
            for ag in af:
                if (ag=='x'):
                    black_count=black_count+1
                elif(ag=='o'):
                    white_count=white_count+1
                else:
                    continue
        if (black_count > white_count):
            print ('You Win !')
            break
        elif(black_count < white_count):
            print ('You Lose !')
            break
        else:
            print ('The game ended in a draw.')
            break
time.sleep(1)
print ('\n\n\n\n\n\n\n\n\n')
print ('A simple reversi game')
time.sleep(1)
print ('\n\n\n\n')
print ('Programmed by Xu Yulong')
time.sleep(1)
print ('\n\n\n\n')
print ('Thanks For Playing')
