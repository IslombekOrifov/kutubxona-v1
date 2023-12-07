def upload_slider_path(instance, image):
    return f"slider/{instance.title}/{image}"

def upload_news_path(instance, file):
    return f"news/{file}"

def upload_center_info_path(instance, file):
    return f"center/info/{file}"

def upload_partner_path(instance, logo):
    return f"partners/logo/{logo}"

def upload_leader_trener_path(instance, image):
    return f"leaderstreners/{image}"

def upload_branch_path(instance, image):
    return f"monitoring/branches/{image}"

def upload_center_structure_path(instance, image):
    return f"center/structure/{image}"

def upload_gallery_path(instance, image):
    return f"gallery/{image}"

def upload_document_path(instance, file):
    return f"documents/{file}"