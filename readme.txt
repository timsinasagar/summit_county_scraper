
To create a virtual environemt, use
    python3 -m venv "project_virtual_environment_name"
        example: python3 -m venv project_env 

To activate a newly created virtual environemt, use
    source project_virtual_environment_name/bin/activate

To deactivate virutual environemt, use
    deactivate

To delete the virtual environemt, use
    rm -rf "project_virtual_environment_name"/

To capture the packages with the version number, use 
    pip freeze > requirements.txt
