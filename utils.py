import gitlab
import base64


def gitlab_object(uri, access_token):
    """
    Gitlab

    """
    gl = gitlab.Gitlab(url=uri, private_token=access_token, ssl_verify=False)
    return gl


def get_projects(gl):
    """
    Returns projects list of tuples


    """
    projects = gl.projects.list(all=True)
    result = [(project.id, project.name) for project in projects]
    return result


def get_project_file(gl, id, file_name):
    """
    Return content of ci_file for project id
    If
        tree not found: content = ERROR,
        ci_file not found: content = NONE

    """

    content = "NONE"
    project = gl.projects.get(id)
    try:
        items = project.repository_tree()

        for item in items:
            if item["name"] == file_name:
                file_info = project.repository_blob(item["id"])
                content = base64.b64decode(file_info['content'])
    except:
        print(f"not found tree for id:{id}")
        content = "ERROR"
    return content
