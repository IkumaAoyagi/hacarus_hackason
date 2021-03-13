import pickle

#このファイルを実行して、projectsのディクショナリを初期化
# projects_dict.pklとして保存

projects = {}

with open("projects_dict.pkl","wb") as f:
    pickle.dump(projects, f)
