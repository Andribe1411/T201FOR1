import threading


def counter_odd(x):
    counter = 0
  
    while counter < x:
        l = True
        if counter % 2 != 0:
            
            if l:
                file = open("test1.txt", "r+", encoding="utf-8")
                b = file.read()
                print(b)
                file.close()
                l = False
            with open('test1.txt', 'w'):
                pass
            file = open("test1.txt", "w", encoding="utf-8")
            file.write(b)
            file.write("\n" + str(counter))
            file.close()
        if counter == x-1:
            l = True



            '''
            file = open("test1.txt", "r+", encoding="utf-8")
            b = file.read()
            file.truncate(0)
            file.write(b)
            print(b)
            file.write(str(counter))
            '''
            """
            for y in file:
                file.write(str(y))
            file.write(str(counter))
            print(counter)
            file.close()
            """
        counter += 1


def counter_even(x):
    counter = 0
    while counter < x:
        if counter % 2 == 0:
            file = open("test2.txt", "r+", encoding="utf-8")
            file.read()
            file.write("\n" + str(counter))
            file.close()
        counter += 1



if __name__ =="__main__":
    t1 = threading.Thread(target=counter_odd, args=(10,))
    t2 = threading.Thread(target=counter_even, args=(10,))
 
    t1.start()
    t2.start()
 
    t1.join()
    t2.join()
 
    print("Done!")