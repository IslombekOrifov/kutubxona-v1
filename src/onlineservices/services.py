def upload_contract_user_path(instance, passport_file):
    return f"contracts/{instance.full_name}/passport/{passport_file}"

def upload_contract_file_path(instance, contract_file):
    return f"contracts/{instance.full_name}/contract/{contract_file}"