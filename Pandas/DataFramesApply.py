import pandas as pd 
df = pd.read_csv("8-apply_function_data.csv")
print(df)
print("******************************************************")

# kolon isimlerini ogrenme
print(df.columns)
print("******************************************************")

print(df["Salary"].mean())
print("******************************************************")


# ortalama 77500 e gore yeni kategori ekleyip maaslarina gore deger ekleyecegiz
def salaryCategory(salary):
    if salary < 50000:
        return "Low"
    elif 50000 <= salary < 80000:
        return "Medium"
    else:
        return "High"

df["SalaryCategory"] = df["Salary"].apply(salaryCategory)
print(df)
print("******************************************************")

# if experience > 10 ise performance_score +1 

def performanceScoreIncrease(experience): 
    if experience > 10: 
        return 1
    else: 
        return 0
    
df["New Score"] = df["Experience"].apply(performanceScoreIncrease) + df["Performance_Score"]
print(df)
print("******************************************************")


# isimdeki _ isaretlerini boslukla degistirecegiz

df["FormattedName"] = df["Name"].apply(lambda x : x.replace("_", " "))
print(df)
print("******************************************************")