import matplotlib.pyplot as plt
import sys
import pickle

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

def single(time, to_plt, model_num, limit):
	fig = plt.figure(figsize=(20, 20))

	plt.subplot(211)
	plt.plot(time[:limit], to_plt[0][:limit], label='Model ' + str(model_num) + ' Imm mRNA')
	plt.plot(time[:limit], to_plt[1][:limit], label='Model ' + str(model_num) + ' Col mRNA')

	plt.ylabel('mRNA present')
	plt.legend(loc = 1)

	xcoords = [(24*60) - 1, 48*60]
	for xc in xcoords:
		plt.axvline(x=xc, color='r', ls='dashed')

	plt.text((24*60) - 1 + 0.1, 100, 'col transformation', rotation=90, color='r')
	plt.text(48*60 + 0.1, 100, 'maxicell induction', rotation=90, color='r')

	plt.subplot(212)
	plt.plot(time[:limit], to_plt[2][:limit], label='Model ' + str(model_num) + ' Imm2')
	plt.plot(time[:limit], to_plt[3][:limit], label='Model ' + str(model_num) + ' Colicin E2')

	plt.xlabel('Time (minutes)')
	plt.ylabel('Protein present')
	plt.legend(loc = 1)

	xcoords = [(24*60) - 1, 48*60]
	for xc in xcoords:
		plt.axvline(x=xc, color='r', ls='dashed')

	plt.savefig('single.png')

if __name__ == '__main__':
    model_num = sys.argv[1]
    limit = sys.argv[2]

    to_plt = load(model_num)

    time = list(range(288*60))

    plt.switch_backend('agg')

    single(time, to_plt, model_num, int(limit))
