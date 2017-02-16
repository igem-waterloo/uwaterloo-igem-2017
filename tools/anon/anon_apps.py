import csv


class Anon(object):

    def __init__(self, applications_csv):
        self.applications_csv = applications_csv
        self.SUBTEAM_COL = 14
        self.EMAIL_COL = 1
        self.NAME_COL = 2
        self.ALL_RANGE = range(3, 14) + [42, 43, 50]
        self.LAB_RANGE = range(15, 24)
        self.MATH_RANGE = range(24, 28) + [41]
        self.POLICY_RANGE = range(28, 36)
        self.BUSINESS_RANGE = range(36, 40)
        self.NAME_KEY = 'name_key.csv'
        self.SUBTEAM_MAPPINGS = {
            "LAB": "Lab and Design",
            "MAT": "Mathematical Modelling",
            "PNP": "Policy and Practices",
            "BUS": "Business and Administration"
        }

    def anonymizeApplications(self):

        def answer_in_range(col_range, app):
            for i in col_range:
                if len(app[i]) > 0:
                    return True
            return False

        with open(self.applications_csv, 'r') as f:
            apps = csv.reader(f, delimiter=',', quotechar='"')
            names = []

            for i, app in enumerate(apps):
                if i == 0:
                    col_names = app
                    continue
                names.append('{}, {}'.format(app[self.NAME_COL], app[self.EMAIL_COL]))
                app_file_name = "Applicant_{}_".format(i)
                subteam_apps = {}
                if answer_in_range(self.MATH_RANGE, app):
                    subteam_apps["MAT"] = self.ALL_RANGE + self.MATH_RANGE
                if answer_in_range(self.LAB_RANGE, app):
                    subteam_apps["LAB"] = self.ALL_RANGE + self.LAB_RANGE
                if answer_in_range(self.POLICY_RANGE, app):
                    subteam_apps["PNP"] = self.ALL_RANGE + self.POLICY_RANGE
                if answer_in_range(self.BUSINESS_RANGE, app):
                    subteam_apps["BUS"] = self.ALL_RANGE + self.BUSINESS_RANGE

                for subteam in subteam_apps:
                    html_out = """<html><head><style type=\"text/css\">
                                div.wrapper {{
                                width: 700px;
                                padding: 20px 50px;
                                background: #d6dcde;
                                font-family: Helvetica, Sans-serif;
                                }}
                                </style></head>
                                <body>
                                <div class=\"wrapper\">
                                <h1>Applicant_{}</h1>
                                <h2>{}</h2>""".format(i, self.SUBTEAM_MAPPINGS[subteam])

                    for col in subteam_apps[subteam]:
                        question = col_names[col]
                        answer = app[col]
                        html_out += '<b>{}</b>: {} <br /><br />\n'.format(question, answer)

                    html_out += "</div></body></html>"

                    with open(app_file_name + subteam + ".html", 'w') as app_file:
                        app_file.write(html_out)

            name_key = ['{}, {}'.format(i + 1, name) for i, name in enumerate(names)]
            with open(self.NAME_KEY, 'w') as nk:
                nk.write('\n'.join(name_key))


if __name__ == '__main__':
    a = Anon('waterloo_igem_2017_application__responses__-_form_responses_1.csv')
    a.anonymizeApplications()
