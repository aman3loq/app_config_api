from src.instance.service_instance import db

# db add, commit, flush and refresh
def db_push(obj):
    db.session.add(obj)
    db.session.commit()
    db.session.flush()
    db.session.refresh(obj)

def db_update(obj):
    db.session.merge(obj)
    db.session.commit()
    db.session.flush()

def db_rollback():
    db.session.rollback()

# def get_all_cfg_query(template_id):
#     return "SELECT * FROM config_template LEFT JOIN config_section " \
#            "ON config_template.section_id = config_section.section_id " \
#            "WHERE template_id = " + str(template_id) + ";"

def fetch_template_query(template_id):
    return "SELECT * FROM cfg_template WHERE tamplate_id = " + str(template_id) + ";"

def fetch_config_query(config_name):
    return "SELECT * FROM cfg WHERE saved_name = " + config_name + ";"

def fetch_template_list_query():
    return "SELECT template_id, template_name, created_on, created_by FROM cfg_template;"

def fetch_config_list_query():
    return "SELECT template_id, template_name, saved_name, created_on, created_by FROM cfg;"

