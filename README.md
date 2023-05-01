# Export GitLab CI Files to CSV

This script exports the content of all `.gitlab-ci.yml` files in a GitLab instance to a CSV file.

## Installation

To use this script, you'll need to install the required dependencies first. You can do this by running the following command:

```
pip install -r requirements.txt
```

## Usage

1. Create a `.env` file with the following variables:

```
GITLAB_URL=<your GitLab instance URL>
GITLAB_TOKEN=<your GitLab personal access token>
```

2. Run the `export_to_csv.py` script:

```
python export_to_csv.py
```

This will export the content of all `.gitlab-ci.yml` files in your GitLab instance to a CSV file located in the `export` folder.

## Dependencies

This script requires the following Python packages:

- `python-dotenv==0.19.2`
- `python-gitlab==3.1.1`

## Code Explanation

The `export_to_csv.py` script uses the following functions from the `utils.py` file:

- `gitlab_object`: Connects to a GitLab instance using the `python-gitlab` library.
- `get_projects`: Returns a list of GitLab projects (id and name).
- `get_project_file`: Returns the content of a specific file in a GitLab project.

The `export_to_csv` function loops through all GitLab projects, gets the content of the `.gitlab-ci.yml` file for each project, and saves the data to a CSV file using the `csv` library.

The script also uses the `dotenv` library to load environment variables from the `.env` file.


# gitlab-api
Gitlab Project Content Parser

# usage
pip install -r requirements.txt

create .env file with content:

GITLAB_URL=https://gitlab.example.com

GITLAB_TOKEN=Your Token
