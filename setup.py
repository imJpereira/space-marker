import cx_Freeze
executaveis = [ 
               cx_Freeze.Executable(script="main.py", icon="assets/icon.ico") ]
cx_Freeze.setup(
    name = "Space Marker",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["assets", "scripts"]
        }
    }, executables = executaveis
)