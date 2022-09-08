import os
# файл переместить в папку куда должны быть перенесены фото,
# фото должны быть в папке DCIM, которая должна быть в той же папке что и скрипт
cur_dir = os.path.dirname(os.path.abspath("photomover.py"))
list_f = os.listdir("DCIM")
new_name = 0
for fold_name in list_f:
    for file_name in os.listdir(f"DCIM\\{fold_name}"):
        try:
            old_name, ph_format = file_name.split(".")
        except:
            old_name, ph_format0, ph_format = file_name.split(".")
        os.rename(f"{cur_dir}\\DCIM\\{fold_name}\\{file_name}", f"{cur_dir}\\{new_name}.{ph_format}")
        new_name += 1



