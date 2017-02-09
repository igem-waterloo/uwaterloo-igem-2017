import csv

def anonymizeApplications(applications_csv, name_cols, grouping_cols,
        info_cols, subheading_cols, question_cols):
    with open(applications_csv, 'r') as f:
        apps = csv.reader(f, delimiter=',', quotechar='"')
        num_apps = len(apps)
        name_key = ['{}, {}'.format(i, name) for i, name in enumerate(apps)]
        with open('name_key.csv', 'w') as nk:
            nk.write('\n'join(name_key))
        for i, app in enumerate(apps):
            if i == 0:
                col_names = app
                continue
            app_file_name = "Applicant_{}_".format(i)
            subteam = app[grouping_cols[1]]
            if "Math" in subteam:
                app_file_name += "MAT"
            elif "Lab" in subteam:
                app_file_name += "LAB"
            elif "Policy" in subteam:
                app_file_name += "PNP"
            else:
                app_file_name += "BUS"
            app_file_name += ".html"

            html_out = "<html><head><style type=\"text/css\"> \
               		    div.wrapper { \
               		    width: 700px; \
               		    padding: 20px 50px; \
               		    background: #d6dcde; \
               		    font-family: Helvetica, Sans-serif; \
               		    } \
               		    </style></head> \
               		    <body> \
               		    <div class=\"wrapper\"> \
               		    <h1>Applicant_{}</h1> \
               		    <h2>{}</h2>".format(i, app[subheading_cols])
            for col in info_cols:
                question = col_names[col]
                answer = app[col]
                html_out += '<b>{}</b>: {} <br />\n'.format(question, answer)
            html_out += "</div></body></html>"
            with open(app_file_name, 'w') as app_file:
                app_file.write(html_out)

                
