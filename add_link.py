file='fake_zebra.txt'
model='ImagenetZebra_cycle_attn_X2'
new_file='link_'+model+'_'+file
fileWrite = open(new_file, 'w')
fileRead=open(file)  
line=fileRead.readline()
while (''!=line):
	new_line='https://raw.githubusercontent.com/napCC/PhotoRep/master/'+model+'_'+file[:-4]+'/'+line[:-5]+'_fake_B.png\n'
	fileWrite.write(new_line)
	print('writing : '+line)
	line=fileRead.readline()
fileWrite.close()
fileRead.close()	
print('complete!')
