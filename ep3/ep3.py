import pandas as pd
import matplotlib.pyplot as plt

ejudge = pd.read_html('results_ejudge.html')[0]
info   = pd.read_excel('students_info.xlsx')

#_____________________FAC_GROUPS_______________________#

data = []

fac_groups = pd.unique(info['group_faculty'])

for gr in fac_groups:
	frame    = info.loc[info['group_faculty'] == gr]
	students = pd.unique(frame['login'])
	frame1   = ejudge.loc[ejudge['User'].isin(students)]
	data.append(frame1['Solved'].sum()/len(frame1)) 

plot_data = pd.DataFrame({
	"average_solved" : data,
	"faculty_group"  : fac_groups
	})
plot_data.plot.bar(x='faculty_group', y='average_solved', rot=0)
plt.ylabel('average solved')
plt.title('solved by faculty groups')
plt.grid()
plt.show()

#_____________________INF_GROUPS_______________________#

data = []

inf_groups = pd.unique(info['group_out'])

for gr in inf_groups:
	frame    = info.loc[info['group_out'] == gr]
	students = pd.unique(frame['login'])
	frame1   = ejudge.loc[ejudge['User'].isin(students)]
	data.append(frame1['Solved'].sum()/len(frame1)) 

plot_data = pd.DataFrame({
	"average_solved" : data,
	"group_out"  : fac_groups
	})
plot_data.plot.bar(x='group_out', y='average_solved', rot=0)
plt.ylabel('average solved')
plt.title('solved by informatics groups')
plt.grid()
plt.show()
