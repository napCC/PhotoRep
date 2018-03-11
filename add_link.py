file='real_apple/list.txt'
#model='ImagenetTiger_cycle_attn_X3_fake_tiger'
model='real_orange'
new_file=model+'/'+'link_list'+'.txt'
fileWrite = open(new_file, 'w')
fileRead=open(file)  
line=fileRead.readline()
while (''!=line):
	new_line='https://raw.githubusercontent.com/napCC/PhotoRep/master/'+model+'/'+line[:-5]+'_real_B.png\n'
	fileWrite.write(new_line)
	print('writing : '+new_line)
	line=fileRead.readline()
fileWrite.close()
fileRead.close()	
print('complete!')
