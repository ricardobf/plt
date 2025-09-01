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

### Create Project

```bash
plt bitbucket create-project --workspace plt-workspace --key PLT --name "PLT Project" --is-private
```

### Create Repository

```bash
plt bitbucket create-repo --workspace plt-workspace --repo plt-repo --project-key PLT --is-private
```

### Grant User Access to Repository

```bash
plt bitbucket grant-user --workspace plt-workspace --repo plt-repo --user-uuid "{user-uuid}" --permission write
```


## Tests

### Run
```bash
python -m pytest -v
```