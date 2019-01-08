from src.instance.service_instance import db

class Config_tbl(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    template_id = db.Column(db.Integer)
    template_name = db.Column(db.String(35))
    section_id = db.Column(db.Integer)
    section_name = db.Column(db.String(30))
    key = db.Column(db.String(35))
    value = db.Column(db.String(200))

    def __init__(self,sno,template_id,template_name,section_id,section_name,key,value):
        self.sno = sno
        self.template_id = template_id
        self.template_name = template_name
        self.section_id = section_id
        self.section_name = section_name
        self.key = key
        self.value = value

    def __repr__(self):
        return '{"sno":"%s","template_id":"%s","template_name":"%s","section_id":"%s","section_name":"%s","key":"%s","value":"%s"}' % \
               (self.sno, self.template_id, self.template_name, self.section_id, self.section_name, self.key, self.value)


class Config_section(db.Model):
    section_id = db.Column(db.Integer, primary_key=True)
    parent_section_id = db.Column(db.Integer)

    def __init__(self,section_id,parent_section_id):
        self.section_id = section_id
        self.parent_section_id = parent_section_id

    def __repr__(self):
        return '{"section_id":"%s", "parent_section_id":"%s"}' % (self.section_id, self.parent_section_id)


class Cfg(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    template_id = db.Column(db.Integer)
    template_name = db.Column(db.String(35))
    saved_name = db.Column(db.String(40))
    created_on = db.Column(db.Date)
    created_by = db.Column(db.String(50))
    cfg_json = db.Column(db.String)

    def __init__(self, template_id, template_name, saved_name, created_on, created_by, cfg_json):

        self.template_id = template_id
        self.template_name = template_name
        self.saved_name = saved_name
        self.created_on = created_on
        self.created_by = created_by
        self.cfg_json = cfg_json

    def __repr__(self):
        return '{"sno":"%s", "template_id":"%s", "template_name":"%s", "saved_name":"%s", ' \
               '"created_on":"%s", "created_by":"%s", "cfg_json":"%s"}' % \
               (self.sno, self.template_id, self.template_name, self.saved_name,
                self.created_on, self.created_by, self.cfg_json)

class Cfg_template(db.Model):
    template_id = db.Column(db.Integer, primary_key=True)
    template_name = db.Column(db.String(35))
    created_on = db.Column(db.Date)
    created_by = db.Column(db.String(50))
    template = db.Column(db.String)

    def __init__(self, template_name, created_on, created_by, template):

        self.template_name = template_name
        self.created_on = created_on
        self.created_by = created_by
        self.template = template

    def __repr__(self):
        return '{"template_id":"%s", "template_name":"%s", "created_on":"%s", ' \
               '"created_by":"%s", "template":"%s"}' % \
               (self.template_id, self.template_name, self.created_on,
                self.created_by, self.template)

