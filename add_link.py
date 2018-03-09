file='fake_zebra.txt'
model='ImagenetZebra_cycle_attn_X2_test200_fake_zebra'
#model='real_horse'
new_file='link_'+model+'.txt'
fileWrite = open(new_file, 'w')
fileRead=open(file)  
line=fileRead.readline()
while (''!=line):
	new_line='https://raw.githubusercontent.com/napCC/PhotoRep/master/'+model+'/'+line[:-5]+'_fake_B.png\n'
	fileWrite.write(new_line)
	print('writing : '+new_line)
	line=fileRead.readline()
fileWrite.close()
fileRead.close()	
print('complete!')
