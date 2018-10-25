import sys

if __name__ == '__main__':
	time = float(sys.argv[1])
	with open('records/model_rec.txt') as f:
		results = f.readlines()

	act_times = [float(i[:-5]) for i in results[5::6]]
	closest = min(act_times, key=lambda x:abs(x - time))
	print('Model: ' + str(act_times.index(closest) + 1) + ' is the best candidate.')
	print('Activation Time: ' + str(closest) + ' hrs')
