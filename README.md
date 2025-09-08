# plt
PLT CLI Tool  
A Python CLI that performs common Bitbucket/GitHub admin tasks.

## Quickstart

```bash
# Setup virtual environment
python -m venv .venv && source .venv/bin/activate

# Install dependencies
pip install -e .

# Copy environment template and configure credentials
cp .env.example .env
# Edit .env with your Bitbucket OAuth Client ID and Secret, and GitHub Username and Access Token
```

## Recompile requirements.txt file

```bash
pip-compile --output-file=requirements.txt pyproject.toml
```

## Bitbucket Usage

### List Projects

```bash
plt bitbucket project --action list --workspace plt-workspace
```

### Create/Delete Project

```bash
plt bitbucket project --action [create/delete] --workspace plt-workspace --key PLT --name "PLT Project" --is-private
```

### List User Permissions - Project

```bash
plt bitbucket project --action list-user-permissions --workspace plt-workspace --key PLT
```

### Grant/Revoke User Permissions - Project

```bash
plt bitbucket project --action [grant/revoke]-user-permissions --workspace plt-workspace --key PLT --user-uuid "{user_uuid}" --permission write
```

### Create/Delete Repository

```bash
plt bitbucket repository --action [create/delete] --workspace plt-workspace --key plt-repo --project-key PLT --is-private
```

### List User Permissions to a given Repository

```bash
plt bitbucket repository --action list-user-permissions --workspace plt-workspace --key plt-repo
```

### Grant User Access to a given Repository

```bash
plt bitbucket repository --action grant-user-permission --workspace plt-workspace --key plt-repo --user-uuid "{user_uuid}" --permission write
```

### List User Permissions in Workspace

```bash
plt bitbucket workspace --action list-user-permissions --workspace plt-workspace 
```

### Configure Branch Permission to a given Repository

```bash
plt bitbucket repository --action configure-branch-permissions --workspace plt-workspace --key plt-repo --branch main --user-uuid "{user_uuid}"
```

## GitHub Usage

### List Repositories

```bash
plt github repository --action list
```

### Create/Delete Repository

```bash
plt github repository --action [create/delete] --name plt-repo
```

## Tests

### Run
```bash
python -m pytest -v
```