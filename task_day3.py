#Number 1
dt_mhs = {'Name': 'M.Fajar', 'ID': '51418977'}
dt_matkul = {'lecture': 'Programming', 'Grade': 'A'}

Result = dt_mhs | dt_matkul

print(Result) 

#Number 2
Result.pop('Ma', None)
print(Result)