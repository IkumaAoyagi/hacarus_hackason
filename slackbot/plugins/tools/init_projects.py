import pickle

#このファイルを実行して、projectsのディクショナリを初期化
# projects_dict.pklとして保存
# 新入社員のためのhacarusのonboardingをデフォルトで追加
projects = {"hacarus" : "https://sites.google.com/hacarus.com/student-engineer/attendance?authuser=1"}

with open("projects_dict.pkl","wb") as f:
    pickle.dump(projects, f)
