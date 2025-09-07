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
# Edit .env with your Bitbucket OAuth Client ID and Secret
```

## Usage

### List Projects

```bash
plt bitbucket project --action list --workspace plt-workspace
```

### Create Project

```bash
plt bitbucket project --action create --workspace plt-workspace --key PLT --name "PLT Project" --is-private
```

### Delete Project

```bash
plt bitbucket project --action delete --workspace plt-workspace --key PLT
```

### Create Repository

```bash
plt bitbucket repository --action create --workspace plt-workspace --repo plt-repo --project-key PLT --is-private
```

### Delete Repository

```bash
plt bitbucket repository --action delete --workspace plt-workspace --repo plt-repo --project-key PLT
```

### List User Permissions to a given Repository

```bash
plt bitbucket repository --action list-user-permissions --workspace plt-workspace --repo plt-repo
```

### Grant User Access to a given Repository

```bash
plt bitbucket repository --action grant-user-permission --workspace plt-workspace --repo plt-repo --user-uuid "{user_uuid}" --permission write
```

### List User Permissions in Workspace

```bash
plt bitbucket workspace --action list-user-permissions --workspace plt-workspace 
```

## Recompile requirements.txt file

```bash
pip-compile --output-file=requirements.txt pyproject.toml
```

## Tests

### Run
```bash
python -m pytest -v
```