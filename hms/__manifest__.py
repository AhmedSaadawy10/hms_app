{
    "name": "Hospital Management System",
    "author": "Ahmed Saadawy",
    "description": """the HMS module enhances operational efficiency,
               improves patient care quality,
               and ensures better coordination and communication among healthcare stakeholders
               within a hospital or healthcare organization.
    "summary": "This is the System for Management Hospital and assignment patients Information""",
    "data": [
        # "reports/patient_print.xml",
        # "security/ir.model.access.csv",
        # "security/hms_security.xml",
        "views/base_menus.xml",
        "views/patient_view.xml",
        "views/department_view.xml",
        "views/doctor_view.xml",
        # "views/customer_inherit_view.xml",
        'wizard/add_history_wizard.xml',

    ],
    'depends': ['base', 'web', 'mail'],
}
