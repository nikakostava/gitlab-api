import csv
import sys
import utils
import os


def export_to_csv(src, dst):
    # Store final result List of Lists
    result = []

    # Connect to Gitlab
    gl = utils.gitlab_object(os.environ.get("GITLAB_URL"), os.environ.get("GITLAB_TOKEN"))

    # Get Projects list [(id, name)]
    projects = utils.get_projects(gl)

    # Get ci content for each project
    for project in projects:
        id = project[0]
        name = project[1]
        content = utils.get_project_file(gl, id, src)
        project_data = [id, name, content]
        result.append(project_data)

    # Save result to CSV
    fields = ["ID", "Name", "Content"]
    with open(dst, "w") as file:
        writer = csv.writer(file, sys.stdout, lineterminator="\n")
        writer.writerow(fields)
        writer.writerows(result)


if __name__ == "__main__":
    export_to_csv(".gitlab-ci.yml", "export\\ymlContent.csv")

