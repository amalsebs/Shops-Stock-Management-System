import pickle
d={ "SHOES":0 , "SLIPPERS":0 , "BOOTS":0 }
list=[ "SHOES" , "SLIPPERS" , "BOOTS" ]
fd=open("filed.txt","w")
fl=open("filel.txt","w")
pickle.dump(d,fd)
pickle.dump(list,fl)
fd.close()
fl.close()
flag=1
while(flag==1):
	print "For Addition (ENTER 1)"
	print "For Removal (ENTER 2)"
	print "For Showing Items (ENTER 3)"
	print "To exit (ENTER 4)"
	choice=input("Enter your choice = ")
	flag=1
	fd=open("filed.txt","r")
        fl=open("filel.txt","r")
        list=pickle.load(fl)
        d=pickle.load(fd)
        fd.close()
        fl.close()
	if(choice==1):
		item=raw_input("ENTER THE ITEM NAME = ")
		quantity=input("ENTER THE QUANTITY = ")
		item1=item.upper()
		if(item1 not in list):
			list.append(item1)
			d[item1]=quantity
		else:
			d[item1]+=quantity
		print "UPDATION SUCCESFULL!"
		print
		print
	elif(choice==2):
		item=raw_input("ENTER THE ITEM NAME = ")
                quantity=input("ENTER THE QUANTITY = ")
                item1=item.upper()
                if(item1 not in list):
			print "ITEM NOT FOUND"
			print
                        print
		elif(d[item1]<quantity):
			print "INSUFFICIENT QUANTITY"
			print
                        print

		else:
			d[item1]-=quantity
			print "UPDATION SUCCESSFULL!"
			print
			print
	elif(choice==3):
		for i in list:
			print i," = ",d[i]
			print
                        print

	elif(choice==4):
		flag=0
	else:
		print "INVALID INPUT"
		print
                print
	fd=open("filed.txt","w")
        fl=open("filel.txt","w")
        pickle.dump(d,fd)
        pickle.dump(list,fl)
        fd.close()
        fl.close()
