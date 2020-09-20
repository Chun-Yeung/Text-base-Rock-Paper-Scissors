import random

com = 'r'
you = 'k'
choice = ["r", "p", "s", "q"]
on = True

while on == True:
	comN = random.randint(0, 2) 
	if comN == 0:
		com = 'r'
	elif comN == 1:
		com = 'p'
	else:
		com = 's'

	while you not in choice:
		you = raw_input("input your choice (r, p, s) \ninput q to quit\n")
		if you not in choice:
			print("please input r, p, s, or q!!!")
			print("<----------------------------------------->")
	
	#drew
	if com == 'r' and you == 'r':
		print("you: Rock	com: Rock \nDrew")
		print("<----------------------------------------->")
	elif com == 'p' and you == 'p':
		print("you: Paper	com: Paper \nDrew")
		print("<----------------------------------------->")
	elif com == 's' and you == 's':
		print("you: Scissors	com: Scissors \nDrew")
		print("<----------------------------------------->")
	#win
	elif com == 'r' and you == 'p':
		print("you: Paper	com: Rock \nYou Win!!!!!")
		print("<----------------------------------------->")
	elif com == 'p' and you == 's':
		print("you: Scissors	com: Paper \nYou Win!!!!!")
		print("<----------------------------------------->")
	elif com == 's' and you == 'r':
		print("you: Rock	com: Scissors \nYou Win!!!!!")
		print("<----------------------------------------->")
	#lose
	elif com == 'p' and you == 'r':
		print("you: Rock	com: Paper \nYou Lose (T^T)")
		print("<----------------------------------------->")
	elif com == 'r' and you == 's':
		print("you: Scissors	com: Rock \nYou Lose (T^T)")
		print("<----------------------------------------->")
	elif com == 's' and you == 'p':
		print("you: Paper	com: Scissors \nYou Lose (T^T)")
		print("<----------------------------------------->")
	#quit
	elif you == 'q':
		on = False

	you = 'k'

	


