import pickle

#このファイルを実行して、projectsのディクショナリを初期化
# projects_dict.pklとして保存

projects = {'eva_project': 'https://docs.google.com/presentation/d/1N2U30XnBs8PrvKt0V-OS8uNSMX1FB0x7iMvZfOCt19w/edit#slide=id.p'}

with open("projects_dict.pkl","wb") as f:
    pickle.dump(projects, f)
