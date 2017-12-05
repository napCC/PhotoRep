file='fake_zebra.txt'
#model='ImagenetZebra_cycle_attn_X2'
model='real_horse'
new_file='link_'+model+'.txt'
fileWrite = open(new_file, 'w')
fileRead=open(file)  
line=fileRead.readline()
while (''!=line):
	new_line='https://raw.githubusercontent.com/napCC/PhotoRep/master/'+model+'/'+line[:-5]+'.jpg\n'
	fileWrite.write(new_line)
	print('writing : '+line)
	line=fileRead.readline()
fileWrite.close()
fileRead.close()	
print('complete!')
