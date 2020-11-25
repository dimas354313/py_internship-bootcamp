#Number 2
dt_mhs = {'Name': 'M.Fajar', 'ID': '51418977'}
dt_matkul = {'Lecture': 'Programming', 'Grade': 'A'}

Result = dt_mhs | dt_matkul

Result.pop('Matkul')
print(Result) 
