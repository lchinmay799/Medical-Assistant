disease=dict()
disease["Heart Attack"]=["heart-pain","shortness of breath","nausea"]
disease["Stroke"]=["weakness","difficulty with speech","dizziness","headache"]
disease["Lung Problem"]=["coughing up blood","difficulty breathing"]
disease["Digestion Problem"]=["black stools","diarrhea","vomiting"]
disease["Joint Problem"]=["pain","stiffness"]
disease["Fever"]=["cold","high temperature","weakness"]
disease["Headache"]=["dizziness","vomiting","weakness"]
c={
	0:"Heart Attack",
	1:"Stroke",
	2:"Lung Problem",
	3:"Digestion Problem",
	4:"Joint Problem",
	5:"Fever",
	6:"Headache"
}
def ret(s):
	e=0
	d=[]
	b=dict()
	for key in disease:
		b[key]=[]
	for i in s:
		for key in disease:
			b[key].append(disease[key].count(i))
	for key in b:
		d.append(b[key].count(1))
	for i in range(len(d)):
		for key in disease:
			if((d[i]==len(disease[key]) or d[i]==max(d)) and max(d)!=0):
				print("You may have "+c[i])
				e+=1
				break
	if(e>=1):
		t=str(input("Do you have any other problem? "))
		if(t=="yes"):
			y=list(map(str,input("Enter the problem: ").split()))
			s.extend(y)
			ret(s)
		elif(t=="no"):
			for i in range(len(d)):
				if((d[i]==len(disease[c[i]])) and max(d)!=0):
					print("You have "+c[i])
			med(d)
		else:
			t=str(input("Enter a valid option (yes/no) : "))

	if(e==0 or max(d)==0):
		print("You don't have any problem... Take Rest :)")
def med(d):
	medicine={
	"Heart Attack":["Aspirin","Nitroglycerin"],
	"Stroke":["Plavix","Activase"],
	"Lung Problem":["Aclidinium","Glycopyrolate"],
	"Digestion Problem":["Bismuth Subsalicylate","Dramamine"],
	"Joint Problem":["Glucosamine", "chondroitin"," omega-3"],
	"Fever":["Nicip","Paracetamol","Dolo-250"],
	"Headache":["Paracetamol"]
	}
	for i in range(len(d)):
			if((d[i]==len(disease[c[i]]) or d[i]==max(d)) and max(d)!=0):
				print("You should take the following medicines for "+c[i])
				for j in range(len(medicine[c[i]])):
					print(str(j+1)+" : "+medicine[c[i]][j])
	if(max(d)==0):
		return
s=list(map(str,input("Enter the symptoms: ").split()))
ret(s)




