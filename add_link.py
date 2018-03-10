file='real_tiger.txt'
#model='ImagenetZebra_cycle_attn_X1_test160_fake_horse'
model='CycleGAN_fake_leopard'
new_file='link_'+model+'.txt'
fileWrite = open(new_file, 'w')
fileRead=open(file)  
line=fileRead.readline()
while (''!=line):
	new_line='https://raw.githubusercontent.com/napCC/PhotoRep/master/'+model+'/'+line[:-6]+'_fake_B.png\n'
	fileWrite.write(new_line)
	print('writing : '+new_line)
	line=fileRead.readline()
fileWrite.close()
fileRead.close()	
print('complete!')
