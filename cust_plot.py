import sys
import pickle
import matplotlib.pyplot as plt

def load(model_num):
	file = open('records/model'+ str(model_num) + 'imm_mRNA_total', 'rb')
	imm_mRNA_total = pickle.load(file)
	file.close()
	file = open('records/model'+ str(model_num) + 'col_mRNA_total', 'rb')
	col_mRNA_total = pickle.load(file)
	file.close()
	file = open('records/model'+ str(model_num) + 'imm_total', 'rb')
	imm_total = pickle.load(file)
	file.close()
	file = open('records/model'+ str(model_num) + 'col_total', 'rb')
	col_total = pickle.load(file)
	file.close()
	return imm_mRNA_total, col_mRNA_total, imm_total, col_total

if __name__ == '__main__':
	model_num = sys.argv[1]
	model_num1 = sys.argv[2]
	model_num2 = sys.argv[3]
	to_plt = load(model_num)
	to_plt1 = load(model_num1)
	to_plt2 = load(model_num2)

	time = list(range(288*60))

	plt.switch_backend('agg')
	fig = plt.figure(figsize=(10, 20))

	#mRNA plots

	plt.subplot(311)
	plt.plot(time[:4000], to_plt[0][:4000], label='Model ' + str(model_num) + ' Imm mRNA')
	plt.plot(time[:4000], to_plt[1][:4000], label='Model ' + str(model_num) + ' Col mRNA')

	plt.ylabel('mRNA Present')
	plt.legend(loc = 5)

	xcoords = [(24*60) - 1, 48*60]
	for xc in xcoords:
		plt.axvline(x=xc, color='r', ls='dashed')

	plt.text((24*60) - 1 + 0.1, 100, 'col transformation', rotation=90, color='r')
	plt.text(48*60 + 0.1, 100, 'maxicell induction', rotation=90, color='r')

	plt.subplot(312)
	plt.plot(time[:4000], to_plt1[0][:4000], label='Model ' + str(model_num1) + ' Imm mRNA')
	plt.plot(time[:4000], to_plt1[1][:4000], label='Model ' + str(model_num1) + ' Col mRNA')

	plt.ylabel('mRNA Present')
	plt.legend(loc = 5)

	xcoords = [(24*60) - 1, 48*60]
	for xc in xcoords:
		plt.axvline(x=xc, color='r', ls='dashed')

	plt.text((24*60) - 1 + 0.1, 100, 'col transformation', rotation=90, color='r')
	plt.text(48*60 + 0.1, 100, 'maxicell induction', rotation=90, color='r')

	plt.subplot(313)
	plt.plot(time[:4000], to_plt2[0][:4000], label='Model ' + str(model_num2) + ' Imm mRNA')
	plt.plot(time[:4000], to_plt2[1][:4000], label='Model ' + str(model_num2) + ' Col mRNA')

	plt.ylabel('mRNA Present')
	plt.xlabel('Time (minutes)')
	plt.legend(loc = 5)

	xcoords = [(24*60) - 1, 48*60]
	for xc in xcoords:
		plt.axvline(x=xc, color='r', ls='dashed')

	plt.text((24*60) - 1 + 0.1, 100, 'col transformation', rotation=90, color='r')
	plt.text(48*60 + 0.1, 100, 'maxicell induction', rotation=90, color='r')

	plt.savefig('comp_mRNA.png')

	#protein plots
	fig = plt.figure(figsize=(10, 20))

	plt.subplot(311)
	plt.plot(time, to_plt[2], label='Model ' + str(model_num) + ' Imm')
	plt.plot(time, to_plt[3], label='Model ' + str(model_num) + ' Col')

	plt.ylabel('Protein Present')
	plt.legend(loc = 1)

	for xc in xcoords:
		plt.axvline(x=xc, color='r', ls='dashed')

	plt.text((24*60) - 1 + 0.1, 10000, 'col transformation', rotation=90, color='r')
	plt.text(48*60 + 0.1, 10000, 'maxicell induction', rotation=90, color='r')

	plt.subplot(312)
	plt.plot(time, to_plt1[2], label='Model ' + str(model_num1) + ' Imm')
	plt.plot(time, to_plt1[3], label='Model ' + str(model_num1) + ' Col')

	plt.ylabel('Protein Present')
	plt.legend(loc = 5)

	for xc in xcoords:
		plt.axvline(x=xc, color='r', ls='dashed')


	plt.subplot(313)
	plt.plot(time, to_plt2[2], label='Model ' + str(model_num2) + ' Imm')
	plt.plot(time, to_plt2[3], label='Model ' + str(model_num2) + ' Col')

	plt.ylabel('Protein Present')
	plt.xlabel('Time (minutes)')
	plt.legend(loc = 1)

	for xc in xcoords:
		plt.axvline(x=xc, color='r', ls='dashed')

	plt.savefig('comp_proteins.png')
