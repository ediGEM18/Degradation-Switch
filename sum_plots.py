with open('records/model_rec.txt') as f:
	recs = f.readlines()

times = []

for i in range(len(recs) - 1)[1:]:
	try:
		times.append(recs[(i*6) - 1])
	except(IndexError):
		break

num_times = [float(t[:-6]) for t in times]

longest = max(num_times)
avg_est = sum(num_times)/len(num_times)

loc_max = [i for i, j in enumerate(num_times) if j == longest]
loc_max_pr = [i+1 for i, j in enumerate(num_times) if j == longest]

shortest = num_times[0]
for time in num_times:
	if time < shortest and time != 0:
		shortest = time
	else:
		continue

loc_min = [i for i, j in enumerate(num_times) if j == shortest]
loc_min_pr = [i+1 for i, j in enumerate(num_times) if j == shortest]

avg = min(num_times, key=lambda x:abs(x-avg_est))

loc_avg = [i for i, j in enumerate(num_times) if j == avg]
loc_avg_pr = [i+1 for i, j in enumerate(num_times) if j == avg]

print('longest activation time models' + str(loc_max_pr))
print('activation times')
for loc in loc_max:
	print(num_times[loc])
print('shortest activation time models ' + str(loc_min_pr))
print('activation times')
for loc in loc_min:
	print(num_times[loc])
print('avg activation time models ' + str(loc_avg_pr))
print('activation times')
for loc in loc_avg:
	print(num_times[loc])
