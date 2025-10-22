from functions.get_files_info import get_files_info
from functions.get_file_contents import get_file_contents
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
   working_dir = "calculator"

   #root_contents = get_files_info(working_dir)
   #print(root_contents)
   # pkg_contents = get_files_info(working_dir,"pkg")
   # print(pkg_contents)
   # bin_contents = get_files_info(working_dir, "/bin")
   # print(bin_contents)
   # old_contnets = get_files_info(working_dir, "../")
   # print(old_contnets)
   # main_file = get_file_contents(working_dir, "main.py")
   # print(main_file)
   # pkg_file = get_file_contents(working_dir, "pkg/calculator.py")
   # print(pkg_file)
   # bin_cat = get_file_contents(working_dir, "/bin/cat")
   # print(bin_cat)
   # not_exist = get_file_contents(working_dir, "pkg/does_not_exist.py")
   # print(not_exist)
   # write_lorem = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
   # print(write_lorem)
   # pkg_lorem = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
   # print(pkg_lorem)
   # not_allowed = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
   # print(not_allowed)
   first_op= run_python_file("calculator", "main.py")
   print(first_op)
   second_op=run_python_file("calculator", "main.py", ["3 + 5"])
   print(second_op)
   third_op= run_python_file("calculator", "tests.py")
   print(third_op)
   forth_op= run_python_file("calculator", "../main.py")
   print(forth_op)
   fifth_op= run_python_file("calculator", "nonexistent.py")
   print(fifth_op)
   sixth_op= run_python_file("calculator", "lorem.txt")
   print(sixth_op)

if __name__ == "__main__":
    main()