from OOPprojectModels import Mentor, Student

mentorsList = []
studentsList = []
while True:
    ch = int(input('\n1.Mentors Management\t2.Students Management\n3.Exit'))
    if ch == 1:
        print('\n-------------Welcome To Mentors Management----------------\n')
        while True:
            mm = int(input('\n1.Show Mentors\t2.Add Mentor\n3.Update Mentor\t4.Delete Mentor\n5.Back to Main Menu'))
            if mm == 1:
                print('\n1.Show Mentors')
                if len(mentorsList) == 0:
                    print('No Mentors Added Yet!!!')
                else:
                    for mentor in mentorsList:
                        print(mentor,end='')
                        print(',Mono:',mentor.getMono(),'\n')
            elif mm == 2:
                print('\n2.Add Mentor')
                n = input('Enter Mentor Name:')
                a = int(input('Enter Mentor Age:'))
                g = input('Enter Mentor Gender:')
                i = int(input('Enter Mentor ID:'))
                s = float(input('Enter Mentor CTC:'))
                mn = input('Enter Mentor Mo No:')
                m1 = Mentor(n,a,g,i,s)
                m1.setMono(mn)
                mentorsList.append(m1)
            elif mm == 3:
                print('\n3.Update Mentor')
                wu=int(input('What Do You Wants To Update : \n Press 1 To Update Age. \n Press 2 To Update CTC. \n Press 3 To Update Mo No.\n press 4 to Go Back'))
                i = int(input('Enter Mentor ID to update:'))
                if wu == 1:
                    for mentor in mentorsList:
                        if mentor.eid == i:
                            new_age = int(input('Enter Age:'))
                            mentor.age = new_age
                            print('Updated New Age Successfully !')
                            
                        else:
                            print('Mentor Id Is Not Vaild')
                elif wu == 2:    
                    for mentor in mentorsList:
                        if mentor.eid == i:
                            s = float(input('Enter Mentor New CTC:'))
                            mentor.esal = s
                            print('Mentor CTC Updated!')
                            
                        else:
                            print('Mentor Id Is Not Vaild')
                elif wu == 3: 
                    for mentor in mentorsList:
                        if mentor.eid == i:
                            new_mn= int(input('Enter New Mo No :'))
                            m1.setMono(new_mn)
                            mentorsList.append(m1)
                            print('Mobile No Updated Successfully!!!')
                            break
                        
                        else:
                            print('Mentor Id Is Not Vaild')
                elif wu == 4:
                    print('****Going Back****')
                    break

                else:
                    print('please enter valid Mentor Id')
                    break
                            
            elif mm == 4:
                print('\n4.Are You Sure Wants To Delete Mentor')
                si = int(input('\n press 1 to Delete. \n Press 2 to Go Back To Main Menu'))
                if si == 1:
                    i = int(input('Enter Mentor ID to delete:'))
                    for mentor in mentorsList:
                        if mentor.eid == i:
                            mentorsList.remove(mentor)
                            print('\n*********Mentor Removed************')
                            
                else:
                    print('Your Data Is Safe Going Back To The Main Menu')
                    break
                
            elif mm == 5:
                print('\n5.Going Back to Main Menu')
                break
            
            else:
                print('\nInvalid Input\n')
    elif ch == 2:
        print('\n----------------Welcome To Students Management--------------------\n')
        while True:
            sm = int(input('\n1.Show Students\t\t2.Add Student\n3.Update Student\t4.Delete Student\n5.Back To Main Menu'))
            if sm == 1:
                print('\n********All Students********')
                if len(studentsList) == 0:
                    print('No Students Added Yet!')
                    
                else:
                    for student in studentsList:
                        print(student,end='')
                        print(',Mono:',student.getMono(),'\n')
            elif sm == 2:
                print('\nTo Add Student Enter Some Details Here:')
                n = input('Enter Student Name:')
                a = int(input('Enter Student Age:'))
                g = input('Enter Student Gender:')
                r = int(input('Enter Student Roll No:'))
                m = float(input('Enter Student Marks:'))
                mn = input('Enter Student Mo No:')
                s1 = Student(n,a,g,r,m)
                s1.setMono(mn)
                studentsList.append(s1)
            elif sm == 3:
                print('\nTo Update Student Information Give Some Details:')
                wu = int(input('What Do You Wants To Update:\n Press 1 If you Wants To Update Marks \n Press 2 If You Wants To Update Mo No \n Press 3 To Go Back'))
                r = int(input('Enter Student Roll No to update:'))
                if wu == 1:
                    for student in studentsList:
                        if student.rn == r:
                            m = float(input('Enter Student New Marks:'))
                            student.marks = m
                            print('Student Marks Updated!')
                            
                        else:
                            print('Student Is Not Valid')
                elif wu == 2:
                    for student in studentsList:
                        if student.rn == r:
                            new_mn= int(input('Enter New Mo No :'))
                            s1.setMono(new_mn)
                            studentsList.append(s1)
                            print('Mobile No Updated Successfully!!!')
                            break
                        
                        else:
                            print('Mentor Id Is Not Vaild')
                elif wu == 3:
                    print('Go Back To Main Menu ')
                    break
                
                else:
                    print('Please Enter Valid Choice')
                    
            elif sm == 4:
                print('\n4.Are You Sure Want To Delete: ')
                si = int(input('\n press 1 to Delete. \n press 2 if you want to go back'))
                if si == 1:
                    r = int(input('Enter Student Roll No to delete:'))
                    for student in studentsList:
                        if student.rn == r:
                            studentsList.remove(student)
                            print('Student Removed')
                else:
                    print('****Going Back To Main Menu****')
                    break
            elif sm == 5:
                print('\n****Going Back To Main Menu****')
                break
            else:
                print('\nInvalid Input\n')
                print('-------Please Enter Valid Input--------')
    elif ch == 3:
        print('\nExiting...\n')
        break
    else:
        print('\nInvalid Input\n')








