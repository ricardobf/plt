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
# Edit .env with your Bitbucket Username and API Token, and GitHub Username and Access Token
```

## Recompile requirements.txt file

```bash
pip-compile --output-file=requirements.txt pyproject.toml
```

## Bitbucket Usage

### List Projects

```bash
plt --provider bitbucket --resource project --action list --workspace plt-workspace
```

### Create/Delete Project

```bash
plt --provider bitbucket --resource project --action create --workspace plt-workspace --project PLT --is-private
plt --provider bitbucket --resource project --action delete --workspace plt-workspace --project PLT
```

### List User Permissions - Project

```bash
plt --provider bitbucket --resource project --action list --workspace plt-workspace --project PLT --user-permissions
```

### Grant/Revoke User Permissions - Project

```bash
plt --provider bitbucket --resource project --action grant --workspace plt-workspace --project PLT --user-uuid {user_uuid} --permission admin
plt --provider bitbucket --resource project --action revoke --workspace plt-workspace --project PLT --user-uuid {user_uuid}
```

### Create/Delete Repository

```bash
plt --provider bitbucket --resource repository --action create --workspace plt-workspace --repo plt-repo --project PLT --is-private
plt --provider bitbucket --resource repository --action delete --workspace plt-workspace --repo plt-repo --project PLT
```

### List User Permissions to a given Repository

```bash
plt --provider bitbucket --resource repository --action list --workspace plt-workspace --repo plt-repo --user-permissions
```

### Grant/Revoke User Access to a given Repository

```bash
plt --provider bitbucket --resource repository --action grant --workspace plt-workspace --repo plt-repo --user-uuid {user_uuid} --permission write
plt --provider bitbucket --resource repository --action revoke --workspace plt-workspace --repo plt-repo --user-uuid {user_uuid}
```

### List User Permissions in Workspace

```bash
plt --provider bitbucket --resource workspace --action list --workspace plt-workspace --user-permissions
```

### Configure Branch Permission to a given Repository

```bash
plt --provider bitbucket --resource repository --action configure-branch-permissions --workspace plt-workspace --repo plt-repo --branch main --user-uuid {user_uuid}
```

## GitHub Usage

### List Repositories

```bash
plt github repository --action list
```

### Create/Delete Repository

```bash
plt --provider github --resource repository --action create --repo plt-repo
plt --provider github --resource repository --action delete --repo plt-repo
```

## Logging

Logging is currently enabled and the level is set to ERROR only.
If you want to change it for DEBUG, you can run the following command to set it via ENV var:
```bash
export LOG_LEVEL=DEBUG
```

## Tests

### Run
```bash
python -m pytest -v
```